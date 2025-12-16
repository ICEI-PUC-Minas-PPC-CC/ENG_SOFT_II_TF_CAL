"""
Testes unitários para a API de Gerenciamento de Tarefas
Inclui testes que passam e testes que falham intencionalmente
"""

import pytest
import json
import os
import sys
from datetime import datetime

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, DATA_FILE

@pytest.fixture
def client():
    """Fixture para criar cliente de teste"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    # Limpa o arquivo de dados após cada teste
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

# ========== TESTES QUE PASSAM ==========

def test_health_check(client):
    """Teste: Verifica se o endpoint de health check funciona"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_index_endpoint(client):
    """Teste: Verifica se o endpoint raiz retorna informações da API"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'endpoints' in data

def test_create_task_success(client):
    """Teste: Cria uma tarefa com sucesso"""
    task_data = {
        'title': 'Tarefa de teste',
        'description': 'Descrição da tarefa',
        'status': 'pendente'
    }
    response = client.post('/tasks', 
                          data=json.dumps(task_data),
                          content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Tarefa de teste'
    assert data['id'] == 1
    assert data['status'] == 'pendente'

def test_get_all_tasks(client):
    """Teste: Lista todas as tarefas"""
    # Cria algumas tarefas
    for i in range(3):
        task_data = {'title': f'Tarefa {i+1}'}
        client.post('/tasks', 
                   data=json.dumps(task_data),
                   content_type='application/json')
    
    response = client.get('/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['total'] == 3
    assert len(data['tasks']) == 3

def test_get_task_by_id(client):
    """Teste: Busca uma tarefa por ID"""
    # Cria uma tarefa
    task_data = {'title': 'Tarefa específica'}
    create_response = client.post('/tasks',
                                 data=json.dumps(task_data),
                                 content_type='application/json')
    created_task = json.loads(create_response.data)
    task_id = created_task['id']
    
    # Busca a tarefa
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == task_id
    assert data['title'] == 'Tarefa específica'

def test_update_task_success(client):
    """Teste: Atualiza uma tarefa com sucesso"""
    # Cria uma tarefa
    task_data = {'title': 'Tarefa original'}
    create_response = client.post('/tasks',
                                 data=json.dumps(task_data),
                                 content_type='application/json')
    created_task = json.loads(create_response.data)
    task_id = created_task['id']
    
    # Atualiza a tarefa
    update_data = {'title': 'Tarefa atualizada', 'status': 'concluida'}
    response = client.put(f'/tasks/{task_id}',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Tarefa atualizada'
    assert data['status'] == 'concluida'

def test_delete_task_success(client):
    """Teste: Remove uma tarefa com sucesso"""
    # Cria uma tarefa
    task_data = {'title': 'Tarefa para deletar'}
    create_response = client.post('/tasks',
                                 data=json.dumps(task_data),
                                 content_type='application/json')
    created_task = json.loads(create_response.data)
    task_id = created_task['id']
    
    # Remove a tarefa
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200
    
    # Verifica se foi removida
    get_response = client.get(f'/tasks/{task_id}')
    assert get_response.status_code == 404

def test_filter_tasks_by_status(client):
    """Teste: Filtra tarefas por status"""
    # Cria tarefas com diferentes status
    statuses = ['pendente', 'em_andamento', 'concluida']
    for status in statuses:
        task_data = {'title': f'Tarefa {status}', 'status': status}
        client.post('/tasks',
                   data=json.dumps(task_data),
                   content_type='application/json')
    
    # Filtra por status
    response = client.get('/tasks?status=pendente')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert all(t['status'] == 'pendente' for t in data['tasks'])

def test_create_task_without_title_fails(client):
    """Teste: Tenta criar tarefa sem título (deve falhar)"""
    task_data = {'description': 'Sem título'}
    response = client.post('/tasks',
                          data=json.dumps(task_data),
                          content_type='application/json')
    assert response.status_code == 400

# ========== TESTES QUE FALHAM INTENCIONALMENTE ==========

def test_task_has_priority_field(client):
    """Teste FALHANDO: Verifica se tarefa tem campo priority (não implementado)"""
    task_data = {'title': 'Tarefa com prioridade', 'priority': 'alta'}
    response = client.post('/tasks',
                          data=json.dumps(task_data),
                          content_type='application/json')
    data = json.loads(response.data)
    # Este teste falha porque o campo priority não é salvo
    assert 'priority' in data
    assert data['priority'] == 'alta'

def test_task_has_due_date(client):
    """Teste FALHANDO: Verifica se tarefa tem data de vencimento"""
    task_data = {
        'title': 'Tarefa com vencimento',
        'due_date': '2024-12-31'
    }
    response = client.post('/tasks',
                          data=json.dumps(task_data),
                          content_type='application/json')
    data = json.loads(response.data)
    # Este teste falha porque due_date não é implementado
    assert 'due_date' in data

def test_update_nonexistent_task_returns_error(client):
    """Teste FALHANDO: Atualiza tarefa inexistente (espera erro específico)"""
    update_data = {'title': 'Tarefa inexistente'}
    response = client.put('/tasks/999',
                         data=json.dumps(update_data),
                         content_type='application/json')
    # Este teste falha porque espera código 400, mas retorna 404
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == 'ID inválido'

def test_task_auto_assigns_user(client):
    """Teste FALHANDO: Verifica se tarefa é atribuída automaticamente a um usuário"""
    task_data = {'title': 'Tarefa atribuída'}
    response = client.post('/tasks',
                          data=json.dumps(task_data),
                          content_type='application/json')
    data = json.loads(response.data)
    # Este teste falha porque atribuição de usuário não está implementada
    assert 'assigned_to' in data
    assert data['assigned_to'] is not None

def test_get_tasks_with_pagination(client):
    """Teste FALHANDO: Verifica paginação de tarefas"""
    # Cria 15 tarefas
    for i in range(15):
        task_data = {'title': f'Tarefa {i+1}'}
        client.post('/tasks',
                   data=json.dumps(task_data),
                   content_type='application/json')
    
    # Tenta buscar com paginação
    response = client.get('/tasks?page=1&per_page=10')
    data = json.loads(response.data)
    # Este teste falha porque paginação não está implementada
    assert 'page' in data
    assert 'per_page' in data
    assert len(data['tasks']) == 10

def test_task_status_validation(client):
    """Teste FALHANDO: Verifica validação de status com valor inválido"""
    task_data = {'title': 'Tarefa', 'status': 'status_invalido'}
    response = client.post('/tasks',
                          data=json.dumps(task_data),
                          content_type='application/json')
    # Este teste falha porque validação de status na criação não está implementada
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'status inválido' in data['error'].lower()

