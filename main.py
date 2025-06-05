from playwright.sync_api import sync_playwright
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.brandili.com.br/")
        print(f"Título da página: {page.title()}")
        browser.close()

if __name__ == "__main__":
    run_test()