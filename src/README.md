# Código Fonte - API de Gerenciamento de Tarefas

## Estrutura do Projeto

```
src/
├── app.py              # Aplicação Flask principal
├── requirements.txt    # Dependências Python
├── Dockerfile          # Configuração Docker
├── pytest.ini         # Configuração pytest
└── tests/
    ├── __init__.py
    └── test_app.py     # Testes automatizados
```

## Instalação

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

## Execução

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ -v --cov=. --cov-report=html
```

## Docker

```bash
# Build
docker build -t todo-api .

# Run
docker run -p 5000:5000 todo-api
```
