#!/bin/bash
# Script para executar testes localmente

echo "Executando testes da aplicação..."

# Ativa ambiente virtual se existir
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Executa testes com cobertura
pytest tests/ -v \
    --junitxml=test-results.xml \
    --cov=. \
    --cov-report=xml \
    --cov-report=html \
    --cov-report=term-missing

echo "Testes concluídos!"
echo "Relatório de cobertura disponível em: htmlcov/index.html"

