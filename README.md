# API de Gerenciamento de Tarefas (TODO API)

`PPC-CC: PUC Poços de Caldas - Ciência da Computação`  
`Disciplina: Engenharia de Software II`  
`2024 - Trabalho Final: Pipeline CI/CD com Jenkins`

## Integrantes

- João Henrique dos Santos Ferreira
- Marcelle Andrade Pereira 
- Nicolas Martins Lorena 
- Vinicius Corrêa de Assis 
- Pedro Balsamão da Costa

## Professor

- Diego Roberto Gonçalves de Pontes

---

## Documentação

- **[Relatório Final](docs/RELATORIO_FINAL.md)** - Relatório completo do trabalho final com prints, casos de teste, arquitetura e conclusões

---

## Descrição do Projeto

Este projeto implementa uma **API REST** para gerenciamento de tarefas (TODO) desenvolvida em **Python/Flask**, com integração completa de **pipeline CI/CD utilizando Jenkins**. A aplicação demonstra práticas de engenharia de software, incluindo desenvolvimento, testes automatizados, build, execução e documentação.

### Funcionalidades da API

- Criar tarefas
- Listar todas as tarefas
- Buscar tarefa por ID
- Atualizar tarefas
- Remover tarefas
- Filtrar tarefas por status
- Health check da API

### Status das Tarefas

- `pendente` - Tarefa ainda não iniciada
- `em_andamento` - Tarefa em execução
- `concluida` - Tarefa finalizada

---

## Arquitetura da Aplicação

```
ENG_SOFT_II_TF_CAL/
│
├── src/
│   ├── app.py                 # Aplicação Flask principal
│   ├── requirements.txt       # Dependências Python
│   ├── Dockerfile             # Configuração Docker
│   ├── pytest.ini            # Configuração pytest
│   └── tests/
│       ├── __init__.py
│       └── test_app.py        # Testes automatizados
│
├── Jenkinsfile               # Pipeline CI/CD
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Este arquivo
```

### Tecnologias Utilizadas

- **Backend**: Python 3.11 + Flask 3.0.0
- **Testes**: pytest 7.4.3 + pytest-cov
- **CI/CD**: Jenkins Pipeline
- **Containerização**: Docker
- **Persistência**: JSON (arquivo local)

---

## Como Executar a Aplicação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- (Opcional) Docker para containerização

### Instalação e Execução Local

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd ENG_SOFT_II_TF_CAL
```

2. **Navegue até o diretório src**:
```bash
cd src
```

3. **Crie um ambiente virtual**:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

4. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

5. **Execute a aplicação**:
```bash
python app.py
```

6. **Acesse a API**:
   - API disponível em: `http://localhost:5000`
   - Health check: `http://localhost:5000/health`
   - Documentação de endpoints: `http://localhost:5000/`

### Execução com Docker (Opcional)

> **Nota**: Docker é opcional. A aplicação funciona perfeitamente sem Docker usando apenas Python.

1. **Certifique-se de que Docker Desktop está rodando** (Windows) ou Docker está ativo (Linux)

2. **Construa a imagem Docker**:
```bash
cd src
docker build -t todo-api .
```

3. **Execute o container**:
```bash
docker run -d -p 5000:5000 --name todo-api todo-api
```

4. **Acesse a API**:
   - `http://localhost:5000`

5. **Parar o container**:
```bash
docker stop todo-api
docker rm todo-api
```

**Problema com Docker?** Não se preocupe! Use a execução local com Python (veja seção acima).

---

## Como Executar os Testes

### Executar todos os testes

```bash
cd src
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pytest tests/ -v
```

### Executar testes com cobertura

```bash
pytest tests/ -v --cov=. --cov-report=html --cov-report=term-missing
```

### Executar testes e gerar relatório JUnit

```bash
pytest tests/ -v --junitxml=test-results.xml
```

### Visualizar relatório de cobertura

Após executar com `--cov-report=html`, abra o arquivo:
```
src/htmlcov/index.html
```

### Testes Implementados

#### Testes que Passam (10 testes)

1. `test_health_check` - Verifica endpoint de health check
2. `test_index_endpoint` - Verifica endpoint raiz
3. `test_create_task_success` - Cria tarefa com sucesso
4. `test_get_all_tasks` - Lista todas as tarefas
5. `test_get_task_by_id` - Busca tarefa por ID
6. `test_update_task_success` - Atualiza tarefa
7. `test_delete_task_success` - Remove tarefa
8. `test_filter_tasks_by_status` - Filtra tarefas por status
9. `test_create_task_without_title_fails` - Valida criação sem título

#### Testes que Falham Intencionalmente (6 testes)

Estes testes foram criados para demonstrar funcionalidades **não implementadas** na aplicação:

1. `test_task_has_priority_field` - Campo de prioridade não implementado
2. `test_task_has_due_date` - Data de vencimento não implementada
3. `test_update_nonexistent_task_returns_error` - Validação de erro específica
4. `test_task_auto_assigns_user` - Atribuição automática de usuário
5. `test_get_tasks_with_pagination` - Paginação de resultados
6. `test_task_status_validation` - Validação de status na criação

**Nota**: Estes testes falham propositalmente para demonstrar o comportamento do pipeline quando há falhas nos testes.

---

## Pipeline CI/CD - Jenkinsfile

O pipeline está configurado no arquivo `Jenkinsfile` na raiz do projeto e contém as seguintes **stages**:

### 1. **Checkout**
- Faz checkout do código do repositório Git
- Exibe informações do último commit

### 2. **Build**
- Cria ambiente virtual Python
- Instala todas as dependências do `requirements.txt`

### 3. **Test**
- Executa todos os testes automatizados
- Gera relatório JUnit XML (`test-results.xml`)
- Gera relatório de cobertura de código
- Publica relatórios no Jenkins

### 4. **Quality Check**
- Verifica qualidade do código
- Valida sintaxe Python

### 5. **Package**
- Empacota artefatos da aplicação
- Cria arquivo com informações do build
- Arquiva artefatos no Jenkins

### 6. **Docker Build**
- Constrói imagem Docker da aplicação
- Taggeia imagem com número do build

### 7. **Deploy**
- Cria diretório de deploy
- Copia arquivos para diretório de deploy
- (Se Docker disponível) Para container antigo e inicia novo

### Post Actions

- **Always**: Limpa workspace
- **Success**: Envia email de sucesso
- **Failure**: Envia email de falha
- **Unstable**: Notifica sobre testes falhando

---

## Relatórios e Métricas

### Relatórios Gerados pelo Jenkins

1. **Relatório JUnit**: Exibe resultados dos testes (passando/falhando)
2. **Relatório de Cobertura**: Mostra porcentagem de código coberto por testes
3. **Artefatos**: Arquivos empacotados do build
4. **Logs**: Logs completos de cada stage do pipeline

### Como Visualizar no Jenkins

1. Acesse o job no Jenkins
2. Clique em um build específico
3. Navegue até "Test Result" para ver relatórios JUnit
4. Navegue até "Relatório de Cobertura de Testes" para ver cobertura
5. Navegue até "Artifacts" para baixar artefatos

---

## Prints do Pipeline

### Pipeline em Execução

<img src="https://github.com/ICEI-PUC-Minas-PPC-CC/ENG_SOFT_II_TF_CAL/blob/main/docs/img/Captura%20de%20tela%202025-12-16%20205452.png" alt="Pipeline Executando">
*Pipeline mostrando todas as stages sendo executadas*

### Status Final

<img src="https://github.com/ICEI-PUC-Minas-PPC-CC/ENG_SOFT_II_TF_CAL/blob/main/docs/img/Captura%20de%20tela%202025-12-16%20210843.png">
*Status UNSTABLE (amarelo) devido aos 6 testes que falham intencionalmente*

### Relatório JUnit

<img src="https://github.com/ICEI-PUC-Minas-PPC-CC/ENG_SOFT_II_TF_CAL/blob/main/docs/img/image.png">
*Relatório JUnit mostrando 9 testes passando e 6 falhando*

### Relatório de Cobertura

<img src="https://github.com/ICEI-PUC-Minas-PPC-CC/ENG_SOFT_II_TF_CAL/blob/main/docs/img/Captura%20de%20tela%2025-12-16%20204541.png" alt="Cobertura">
*Relatório HTML de cobertura de código (94%)*

### Status dos Testes

- **9 testes passando**
- **6 testes falhando** (intencionalmente)

---

## Casos de Teste Documentados

### Casos de Teste - Funcionalidades Principais

| ID | Caso de Teste | Status | Descrição |
|---|---|---|---|
| CT-01 | Health Check | Passa | Verifica se API está respondendo |
| CT-02 | Criar Tarefa | Passa | Cria nova tarefa com título |
| CT-03 | Listar Tarefas | Passa | Retorna todas as tarefas |
| CT-04 | Buscar por ID | Passa | Retorna tarefa específica |
| CT-05 | Atualizar Tarefa | Passa | Modifica dados da tarefa |
| CT-06 | Remover Tarefa | Passa | Deleta tarefa do sistema |
| CT-07 | Filtrar por Status | Passa | Filtra tarefas por status |
| CT-08 | Validação de Título | Passa | Impede criação sem título |
| CT-09 | Prioridade | Falha | Campo não implementado |
| CT-10 | Data Vencimento | Falha | Campo não implementado |
| CT-11 | Paginação | Falha | Funcionalidade não implementada |
| CT-12 | Atribuição Usuário | Falha | Funcionalidade não implementada |


---

## Configuração do Jenkins

> **Não tem Jenkins?** Veja [INSTALAR_JENKINS.md](INSTALAR_JENKINS.md) para instalar, ou use **GitHub Actions** como alternativa (já configurado em `.github/workflows/ci.yml`)!

### Pré-requisitos no Jenkins

1. **Plugins necessários**:
   - Pipeline
   - JUnit Plugin
   - HTML Publisher Plugin
   - Git Plugin
   - Docker Pipeline (opcional)

2. **Configuração do Job**:
   - Tipo: **Pipeline**
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: URL do repositório GitHub
   - Branch: `main` ou `master`
   - Script Path: `Jenkinsfile`

### Executar Pipeline

1. Acesse o job no Jenkins
2. Clique em "Build Now"
3. Acompanhe a execução em tempo real
4. Visualize relatórios após conclusão

---

## Exemplos de Uso da API

### Criar uma Tarefa

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implementar pipeline CI/CD",
    "description": "Configurar Jenkins para automação",
    "status": "em_andamento"
  }'
```

### Listar Todas as Tarefas

```bash
curl http://localhost:5000/tasks
```

### Buscar Tarefa por ID

```bash
curl http://localhost:5000/tasks/1
```

### Atualizar Tarefa

```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Pipeline CI/CD implementado",
    "status": "concluida"
  }'
```

### Filtrar por Status

```bash
curl http://localhost:5000/tasks?status=pendente
```

### Remover Tarefa

```bash
curl -X DELETE http://localhost:5000/tasks/1
```

---

## Conclusões e Aprendizados

### O que foi aprendido:

1. **Integração CI/CD**: Configuração completa de pipeline Jenkins para automação de processos
2. **Testes Automatizados**: Implementação de testes unitários com pytest e geração de relatórios
3. **Containerização**: Uso de Docker para empacotar e deployar aplicações
4. **Boas Práticas**: Aplicação de práticas de engenharia de software (testes, documentação, versionamento)
5. **Automação**: Redução de trabalho manual através de pipelines automatizados
6. **Qualidade de Código**: Uso de ferramentas de cobertura e relatórios para garantir qualidade

### Desafios Enfrentados:

- Configuração inicial do Jenkins
- Integração de relatórios JUnit
- Configuração de ambiente Docker
- Balanceamento entre testes passando e falhando

### Melhorias Futuras:

- Implementar funcionalidades que fazem os testes falharem
- Adicionar testes de integração
- Implementar autenticação e autorização
- Adicionar banco de dados (PostgreSQL/MySQL)
- Implementar paginação e filtros avançados
- Adicionar documentação Swagger/OpenAPI

---

## Licença

Este projeto foi desenvolvido para fins educacionais.

---

## Links Úteis

- [Relatório Final](docs/RELATORIO_FINAL.md) - Relatório completo do trabalho final
- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação pytest](https://docs.pytest.org/)
- [Documentação Jenkins](https://www.jenkins.io/doc/)
- [Documentação Docker](https://docs.docker.com/)

---

**Desenvolvido para demonstrar práticas de CI/CD com Jenkins**
