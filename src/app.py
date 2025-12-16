"""
API REST para Gerenciamento de Tarefas (TODO)
Aplicação desenvolvida para demonstrar pipeline CI/CD com Jenkins
"""

from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Arquivo para persistência de dados
DATA_FILE = 'tasks.json'

def load_tasks():
    """Carrega tarefas do arquivo JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Salva tarefas no arquivo JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    """Endpoint raiz - informações da API"""
    return jsonify({
        'message': 'API de Gerenciamento de Tarefas',
        'version': '1.0.0',
        'endpoints': {
            'GET /tasks': 'Lista todas as tarefas',
            'GET /tasks/<id>': 'Busca uma tarefa por ID',
            'POST /tasks': 'Cria uma nova tarefa',
            'PUT /tasks/<id>': 'Atualiza uma tarefa',
            'DELETE /tasks/<id>': 'Remove uma tarefa',
            'GET /health': 'Verifica saúde da API'
        }
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Lista todas as tarefas"""
    tasks = load_tasks()
    status_filter = request.args.get('status')
    
    if status_filter:
        tasks = [t for t in tasks if t.get('status') == status_filter]
    
    return jsonify({
        'total': len(tasks),
        'tasks': tasks
    }), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Busca uma tarefa por ID"""
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    return jsonify(task), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    """Cria uma nova tarefa"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Título é obrigatório'}), 400
    
    tasks = load_tasks()
    
    # Gera novo ID
    new_id = max([t['id'] for t in tasks], default=0) + 1
    
    new_task = {
        'id': new_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'status': data.get('status', 'pendente'),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente"""
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        task['title'] = data['title']
    if 'description' in data:
        task['description'] = data['description']
    if 'status' in data:
        if data['status'] not in ['pendente', 'em_andamento', 'concluida']:
            return jsonify({'error': 'Status inválido'}), 400
        task['status'] = data['status']
    
    task['updated_at'] = datetime.now().isoformat()
    
    save_tasks(tasks)
    
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Remove uma tarefa"""
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    tasks.remove(task)
    save_tasks(tasks)
    
    return jsonify({'message': 'Tarefa removida com sucesso'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

