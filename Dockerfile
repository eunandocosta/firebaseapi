# Dockerfile

# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho no contêiner
COPY . .

# Instala as dependências do Python
RUN pip install -r requirements.txt

# Expondo a porta onde o aplicativo Flask será executado
EXPOSE 5004

# Comando para rodar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
