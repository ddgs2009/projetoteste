
# Usa a imagem oficial do Playwright com Python
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . /app

# Instala as dependências Python
RUN pip install -r requirements.txt

# Comando de inicialização
CMD ["python", "main.py"]
