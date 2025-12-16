# 📚 Exemplos de Uso da API

Este documento contém exemplos práticos de uso da API de Gerenciamento de Tarefas.

## 🌐 Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Informações da API |
| GET | `/health` | Health check |
| GET | `/tasks` | Lista todas as tarefas |
| GET | `/tasks/<id>` | Busca tarefa por ID |
| POST | `/tasks` | Cria nova tarefa |
| PUT | `/tasks/<id>` | Atualiza tarefa |
| DELETE | `/tasks/<id>` | Remove tarefa |

## 📝 Exemplos com cURL

### 1. Health Check

```bash
curl http://localhost:5000/health
```

**Resposta:**
```json
{
  "status": "healthy",
  "timestamp": "2024-12-16T10:30:00.123456"
}
```

### 2. Informações da API

```bash
curl http://localhost:5000/
```

**Resposta:**
```json
{
  "message": "API de Gerenciamento de Tarefas",
  "version": "1.0.0",
  "endpoints": { ... }
}
```

### 3. Criar Tarefa

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implementar pipeline CI/CD",
    "description": "Configurar Jenkins para automação completa",
    "status": "em_andamento"
  }'
```

**Resposta:**
```json
{
  "id": 1,
  "title": "Implementar pipeline CI/CD",
  "description": "Configurar Jenkins para automação completa",
  "status": "em_andamento",
  "created_at": "2024-12-16T10:30:00.123456",
  "updated_at": "2024-12-16T10:30:00.123456"
}
```

### 4. Listar Todas as Tarefas

```bash
curl http://localhost:5000/tasks
```

**Resposta:**
```json
{
  "total": 2,
  "tasks": [
    {
      "id": 1,
      "title": "Implementar pipeline CI/CD",
      "description": "Configurar Jenkins para automação completa",
      "status": "em_andamento",
      "created_at": "2024-12-16T10:30:00.123456",
      "updated_at": "2024-12-16T10:30:00.123456"
    },
    {
      "id": 2,
      "title": "Escrever testes automatizados",
      "description": "Criar testes unitários com pytest",
      "status": "pendente",
      "created_at": "2024-12-16T10:35:00.123456",
      "updated_at": "2024-12-16T10:35:00.123456"
    }
  ]
}
```

### 5. Buscar Tarefa por ID

```bash
curl http://localhost:5000/tasks/1
```

**Resposta:**
```json
{
  "id": 1,
  "title": "Implementar pipeline CI/CD",
  "description": "Configurar Jenkins para automação completa",
  "status": "em_andamento",
  "created_at": "2024-12-16T10:30:00.123456",
  "updated_at": "2024-12-16T10:30:00.123456"
}
```

### 6. Filtrar Tarefas por Status

```bash
curl http://localhost:5000/tasks?status=pendente
```

**Resposta:**
```json
{
  "total": 1,
  "tasks": [
    {
      "id": 2,
      "title": "Escrever testes automatizados",
      "status": "pendente",
      ...
    }
  ]
}
```

### 7. Atualizar Tarefa

```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Pipeline CI/CD implementado",
    "status": "concluida"
  }'
```

**Resposta:**
```json
{
  "id": 1,
  "title": "Pipeline CI/CD implementado",
  "description": "Configurar Jenkins para automação completa",
  "status": "concluida",
  "created_at": "2024-12-16T10:30:00.123456",
  "updated_at": "2024-12-16T11:00:00.123456"
}
```

### 8. Remover Tarefa

```bash
curl -X DELETE http://localhost:5000/tasks/1
```

**Resposta:**
```json
{
  "message": "Tarefa removida com sucesso"
}
```

## 🐍 Exemplos com Python

```python
import requests

BASE_URL = "http://localhost:5000"

# Criar tarefa
response = requests.post(f"{BASE_URL}/tasks", json={
    "title": "Tarefa Python",
    "description": "Criada via Python",
    "status": "pendente"
})
print(response.json())

# Listar tarefas
response = requests.get(f"{BASE_URL}/tasks")
tasks = response.json()
print(f"Total de tarefas: {tasks['total']}")

# Atualizar tarefa
task_id = 1
response = requests.put(f"{BASE_URL}/tasks/{task_id}", json={
    "status": "concluida"
})
print(response.json())
```

## 🌐 Exemplos com JavaScript (Fetch)

```javascript
const BASE_URL = "http://localhost:5000";

// Criar tarefa
fetch(`${BASE_URL}/tasks`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'Tarefa JavaScript',
    description: 'Criada via JavaScript',
    status: 'pendente'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// Listar tarefas
fetch(`${BASE_URL}/tasks`)
  .then(response => response.json())
  .then(data => console.log(data));
```

## ⚠️ Tratamento de Erros

### Tarefa não encontrada

```bash
curl http://localhost:5000/tasks/999
```

**Resposta (404):**
```json
{
  "error": "Tarefa não encontrada"
}
```

### Criar tarefa sem título

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "Sem título"}'
```

**Resposta (400):**
```json
{
  "error": "Título é obrigatório"
}
```

### Status inválido na atualização

```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "status_invalido"}'
```

**Resposta (400):**
```json
{
  "error": "Status inválido"
}
```

## 📊 Status Válidos

- `pendente` - Tarefa ainda não iniciada
- `em_andamento` - Tarefa em execução
- `concluida` - Tarefa finalizada

---

**Última atualização**: 2024

