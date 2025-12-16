# Script PowerShell para testar a API
# Execute: .\test_api.ps1

$baseUrl = "http://localhost:5000"

Write-Host "`nTestando API de Gerenciamento de Tarefas" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan

# Health Check
Write-Host "`n Health Check:" -ForegroundColor Yellow
try {
    $health = Invoke-RestMethod -Uri "$baseUrl/health" -Method Get
    Write-Host "API está funcionando!" -ForegroundColor Green
    $health | ConvertTo-Json
} catch {
    Write-Host "Erro ao conectar com a API. Certifique-se de que está rodando em http://localhost:5000" -ForegroundColor Red
    exit
}

# Informações da API
Write-Host "`n Informações da API:" -ForegroundColor Yellow
$info = Invoke-RestMethod -Uri "$baseUrl/" -Method Get
$info | ConvertTo-Json

# Criar tarefa
Write-Host "`n Criando nova tarefa..." -ForegroundColor Yellow
$newTask = @{
    title = "Tarefa criada via PowerShell"
    description = "Esta tarefa foi criada usando o script de teste"
    status = "pendente"
} | ConvertTo-Json

try {
    $created = Invoke-RestMethod -Uri "$baseUrl/tasks" -Method Post -Body $newTask -ContentType "application/json"
    Write-Host "Tarefa criada com sucesso!" -ForegroundColor Green
    $created | ConvertTo-Json
    $taskId = $created.id
} catch {
    Write-Host "Erro ao criar tarefa: $_" -ForegroundColor Red
    exit
}

# Listar todas as tarefas
Write-Host "`n Listando todas as tarefas:" -ForegroundColor Yellow
try {
    $allTasks = Invoke-RestMethod -Uri "$baseUrl/tasks" -Method Get
    Write-Host "Total de tarefas: $($allTasks.total)" -ForegroundColor Green
    $allTasks.tasks | ConvertTo-Json -Depth 10
} catch {
    Write-Host " Erro ao listar tarefas: $_" -ForegroundColor Red
}

# Buscar tarefa por ID
Write-Host "`n Buscando tarefa por ID ($taskId):" -ForegroundColor Yellow
try {
    $task = Invoke-RestMethod -Uri "$baseUrl/tasks/$taskId" -Method Get
    $task | ConvertTo-Json
} catch {
    Write-Host " Erro ao buscar tarefa: $_" -ForegroundColor Red
}

# Atualizar tarefa
Write-Host "`n Atualizando tarefa ($taskId)..." -ForegroundColor Yellow
$update = @{
    title = "Tarefa atualizada via PowerShell"
    status = "concluida"
} | ConvertTo-Json

try {
    $updated = Invoke-RestMethod -Uri "$baseUrl/tasks/$taskId" -Method Put -Body $update -ContentType "application/json"
    Write-Host " Tarefa atualizada!" -ForegroundColor Green
    $updated | ConvertTo-Json
} catch {
    Write-Host " bErro ao atualizar tarefa: $_" -ForegroundColor Red
}

# Filtrar por status
Write-Host "`n Filtrando tarefas por status (concluida):" -ForegroundColor Yellow
try {
    $filtered = Invoke-RestMethod -Uri "$baseUrl/tasks?status=concluida" -Method Get
    Write-Host "Tarefas concluídas: $($filtered.total)" -ForegroundColor Green
    $filtered.tasks | ConvertTo-Json -Depth 10
} catch {
    Write-Host " Erro ao filtrar tarefas: $_" -ForegroundColor Red
}

Write-Host "`n Testes concluídos!" -ForegroundColor Green
Write-Host "=" * 50 -ForegroundColor Cyan

