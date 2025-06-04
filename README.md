# Projeto de Validação de Frete - Brandili

## 🔥 Funcionalidades
- Navega no site da Brandili
- Cota frete para capitais e interiores de todos os estados
- Valida adição de produto no carrinho
- Exporta os resultados para CSV e Google Sheets

## 🛠️ Como Rodar Localmente

1. Clone este repositório:

```bash
git clone https://github.com/ddgs2009/projetoteste.git
cd projetoteste
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
playwright install
```

3. Configure a API do Google Sheets:
   - Acesse: [Google Cloud Console](https://console.cloud.google.com/)
   - Crie um projeto e ative a API Google Sheets + API Google Drive
   - Crie uma credencial do tipo Service Account
   - Baixe o JSON e salve como `credentials.json` na raiz do projeto
   - Compartilhe sua planilha com o email da service account

4. Crie uma planilha chamada `Frete Results` no seu Google Sheets.

5. Execute:

```bash
python main.py
```

## ☁️ Deploy na Nuvem (Render.com ou Railway.app)

- Suba este repositório no GitHub.
- Crie um serviço no Render (background worker) ou Railway (cron job).
- Comando de start:

```bash
python main.py
```

## 📄 Estrutura do Projeto

- `main.py`: Script principal
- `ceps.csv`: Lista de CEPs para teste
- `credentials.json.example`: Modelo das credenciais Google
- `requirements.txt`: Dependências
- `.gitignore`: Arquivos ignorados

## 🚀 Feito por ddgs2009