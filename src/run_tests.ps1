# Script PowerShell para executar testes da aplicação

Write-Host "Executando testes da aplicação..." -ForegroundColor Cyan

# Ativa ambiente virtual se existir
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow
    & "venv\Scripts\Activate.ps1"
}

# Executa testes com cobertura
Write-Host "`nExecutando pytest..." -ForegroundColor Green
pytest tests/ -v `
    --junitxml=test-results.xml `
    --cov=. `
    --cov-report=xml `
    --cov-report=html `
    --cov-report=term-missing

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nTestes concluídos com sucesso!" -ForegroundColor Green
} else {
    Write-Host "`n Alguns testes falharam (isso é esperado - 6 testes falham intencionalmente)" -ForegroundColor Yellow
}

Write-Host "`n Relatório de cobertura disponível em: htmlcov\index.html" -ForegroundColor Cyan
Write-Host " Relatório JUnit disponível em: test-results.xml" -ForegroundColor Cyan

