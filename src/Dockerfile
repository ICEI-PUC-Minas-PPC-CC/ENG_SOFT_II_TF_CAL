# Dockerfile para a API de Gerenciamento de Tarefas
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY app.py .
COPY tests/ ./tests/

# Expõe porta da aplicação
EXPOSE 5000

# Variável de ambiente
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando para executar a aplicação
CMD ["python", "app.py"]

