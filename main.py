from playwright.sync_api import sync_playwright
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime


scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Frete Results")
sheet = spreadsheet.sheet1

df_ceps = pd.read_csv('ceps.csv')

def run_automation():
    results = []
    url = "https://www.brandili.com.br/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(url, timeout=60000)
            page.hover('text="Menina"')
            time.sleep(2)
            page.click('a[href*="/menina/"]')

            page.wait_for_selector('a[href*="/produto/"]', timeout=20000)
            page.click('a[href*="/produto/"]')

            page.wait_for_selector('input[name="zipcode"]')

            for index, row in df_ceps.iterrows():
                cep = row['cep']
                estado = row['estado']
                cidade = row['cidade']
                tipo = row['tipo']

                print(f"Testando CEP {cep} - {cidade}/{estado} ({tipo})")

                page.fill('input[name="zipcode"]', cep)
                page.click('button:has-text("Calcular")')

                page.wait_for_timeout(4000)

                try:
                    frete_info = page.inner_text('.shipping-info')
                except:
                    frete_info = "Erro ou não retornado"

                print(f"Resultado: {frete_info}")

                data_row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            estado, cidade, tipo, cep, frete_info]

                sheet.append_row(data_row)

                results.append({
                    'data': data_row[0],
                    'estado': estado,
                    'cidade': cidade,
                    'tipo': tipo,
                    'cep': cep,
                    'frete': frete_info
                })

            try:
                page.click('button:has-text("Comprar")')
                page.wait_for_timeout(2000)
                print("Produto adicionado ao carrinho")
            except:
                print("Erro ao adicionar produto no carrinho")

        except Exception as e:
            print(f"Erro na execução: {e}")

        finally:
            browser.close()

    df_results = pd.DataFrame(results)
    df_results.to_csv('resultado_frete.csv', index=False)
    print("Resultado salvo em resultado_frete.csv")


if __name__ == "__main__":
    run_automation()