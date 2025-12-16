@echo off
REM Script para executar testes localmente no Windows

echo 🧪 Executando testes da aplicação...

REM Ativa ambiente virtual se existir
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Executa testes com cobertura
pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html --cov-report=term-missing

echo ✅ Testes concluídos!
echo 📊 Relatório de cobertura disponível em: htmlcov\index.html

pause

