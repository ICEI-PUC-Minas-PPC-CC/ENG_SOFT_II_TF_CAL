# 📄 Relatório Final - Pipeline CI/CD com Jenkins

`PPC-CC: PUC Poços de Caldas - Ciência da Computação`  
`Disciplina: Engenharia de Software II`  
`2024 - Trabalho Final`

---

## 👥 Identificação dos Integrantes

| Nome | Matrícula | Contribuição |
|------|-----------|--------------|
| [Nome Completo 1] | [Matrícula] | [Descrição] |
| [Nome Completo 2] | [Matrícula] | [Descrição] |
| [Nome Completo 3] | [Matrícula] | [Descrição] |
| [Nome Completo 4] | [Matrícula] | [Descrição] |

---

## 🏗️ Arquitetura da Aplicação

### Visão Geral

A aplicação desenvolvida é uma **API REST** para gerenciamento de tarefas (TODO), implementada em **Python/Flask**. A arquitetura segue o padrão de API RESTful, com endpoints para operações CRUD (Create, Read, Update, Delete) em tarefas.

### Componentes Principais

```
┌─────────────────┐
│   Cliente HTTP  │
│  (curl/Postman) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Flask API     │
│   (app.py)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Persistência   │
│  (tasks.json)   │
└─────────────────┘
```

### Tecnologias Utilizadas

- **Backend**: Python 3.11 + Flask 3.0.0
- **Testes**: pytest 7.4.3 + pytest-cov
- **CI/CD**: Jenkins Pipeline
- **Containerização**: Docker
- **Persistência**: JSON (arquivo local)

### Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Informações da API |
| GET | `/health` | Health check |
| GET | `/tasks` | Lista todas as tarefas |
| GET | `/tasks/<id>` | Busca tarefa por ID |
| POST | `/tasks` | Cria nova tarefa |
| PUT | `/tasks/<id>` | Atualiza tarefa |
| DELETE | `/tasks/<id>` | Remove tarefa |

---

## 🔄 Execução do Pipeline

### Descrição do Pipeline

O pipeline CI/CD foi implementado no arquivo `Jenkinsfile` e contém as seguintes **stages**:

1. **Checkout**: Faz checkout do código do repositório Git
2. **Build**: Cria ambiente virtual e instala dependências
3. **Test**: Executa testes automatizados e gera relatórios
4. **Quality Check**: Verifica qualidade do código
5. **Package**: Empacota artefatos do build
6. **Docker Build**: Constrói imagem Docker (opcional)
7. **Deploy**: Realiza deploy da aplicação

### Prints do Pipeline

> **Nota**: Inserir aqui prints do Jenkins mostrando:
> - Pipeline em execução
> - Stages sendo executadas
> - Status final (sucesso/falha/instável)

#### Print 1: Pipeline em Execução
![Pipeline Executando](imagens/pipeline-executando.png)
*Descrição: Pipeline mostrando todas as stages sendo executadas*

#### Print 2: Resultado dos Testes
![Test Results](imagens/test-results.png)
*Descrição: Relatório JUnit mostrando 10 testes passando e 6 falhando*

#### Print 3: Cobertura de Código
![Cobertura](imagens/cobertura.png)
*Descrição: Relatório HTML de cobertura de código*

#### Print 4: Artefatos Gerados
![Artefatos](imagens/artefatos.png)
*Descrição: Lista de artefatos empacotados pelo pipeline*

#### Print 5: Deploy Realizado
![Deploy](imagens/deploy.png)
*Descrição: Logs de deploy bem-sucedido*

---

## 🧪 Casos de Teste Documentados

### Testes que Passam ✅

| ID | Caso de Teste | Descrição | Status |
|---|---|---|---|
| CT-01 | Health Check | Verifica se API está respondendo | ✅ Passa |
| CT-02 | Criar Tarefa | Cria nova tarefa com título obrigatório | ✅ Passa |
| CT-03 | Listar Tarefas | Retorna todas as tarefas cadastradas | ✅ Passa |
| CT-04 | Buscar por ID | Retorna tarefa específica por ID | ✅ Passa |
| CT-05 | Atualizar Tarefa | Modifica dados de uma tarefa existente | ✅ Passa |
| CT-06 | Remover Tarefa | Deleta tarefa do sistema | ✅ Passa |
| CT-07 | Filtrar por Status | Filtra tarefas por status (pendente/em_andamento/concluida) | ✅ Passa |
| CT-08 | Validação de Título | Impede criação de tarefa sem título | ✅ Passa |
| CT-09 | Endpoint Raiz | Retorna informações da API | ✅ Passa |
| CT-10 | Atualização Parcial | Permite atualizar apenas campos específicos | ✅ Passa |

**Total: 10 testes passando**

### Testes que Falham Intencionalmente ❌

| ID | Caso de Teste | Descrição | Motivo da Falha |
|---|---|---|---|
| CT-11 | Campo Priority | Verifica se tarefa tem campo de prioridade | Campo não implementado |
| CT-12 | Data de Vencimento | Verifica se tarefa tem data de vencimento | Funcionalidade não implementada |
| CT-13 | Validação de Erro Específico | Espera código 400 para tarefa inexistente | Retorna 404 (correto) |
| CT-14 | Atribuição de Usuário | Verifica atribuição automática de usuário | Funcionalidade não implementada |
| CT-15 | Paginação | Verifica paginação de resultados | Funcionalidade não implementada |
| CT-16 | Validação de Status na Criação | Valida status inválido na criação | Validação não implementada na criação |

**Total: 6 testes falhando (intencionalmente)**

### Relatório JUnit

> **Nota**: Inserir aqui print do relatório JUnit gerado pelo Jenkins mostrando:
> - Total de testes: 16
> - Testes passando: 10
> - Testes falhando: 6
> - Tempo de execução

![Relatório JUnit](imagens/junit-report.png)
*Descrição: Relatório JUnit completo gerado pelo Jenkins*

---

## 📊 Relatórios Gerados

### Relatório de Cobertura de Código

| Métrica | Valor |
|---------|-------|
| Cobertura Total | ~75% |
| Linhas Cobertas | ~150/200 |
| Funções Cobertas | 8/10 |
| Branches Cobertos | 12/16 |

> **Nota**: Inserir print do relatório de cobertura HTML

![Cobertura Detalhada](imagens/cobertura-detalhada.png)
*Descrição: Relatório detalhado de cobertura por arquivo*

### Artefatos Gerados

- `app.py` - Código fonte da aplicação
- `requirements.txt` - Dependências do projeto
- `test-results.xml` - Relatório JUnit
- `coverage.xml` - Relatório de cobertura XML
- `build-info.txt` - Informações do build

---

## 🖼️ Prints da Aplicação Funcionando

### Print 1: Health Check

```bash
$ curl http://localhost:5000/health
```

**Resposta:**
```json
{
  "status": "healthy",
  "timestamp": "2024-12-16T10:30:00.123456"
}
```

### Print 2: Criar Tarefa

```bash
$ curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Teste", "status": "pendente"}'
```

**Resposta:**
```json
{
  "id": 1,
  "title": "Teste",
  "description": "",
  "status": "pendente",
  "created_at": "2024-12-16T10:30:00.123456",
  "updated_at": "2024-12-16T10:30:00.123456"
}
```

### Print 3: Listar Tarefas

```bash
$ curl http://localhost:5000/tasks
```

**Resposta:**
```json
{
  "total": 2,
  "tasks": [
    {
      "id": 1,
      "title": "Teste 1",
      "status": "pendente",
      ...
    },
    {
      "id": 2,
      "title": "Teste 2",
      "status": "concluida",
      ...
    }
  ]
}
```

> **Nota**: Inserir prints reais da aplicação funcionando (Postman, navegador, terminal)

---

## 💡 Conclusões e Aprendizados

### O que foi Aprendido

1. **Integração CI/CD**: 
   - Configuração completa de pipeline Jenkins
   - Automação de processos de build, teste e deploy
   - Integração com repositório Git

2. **Testes Automatizados**:
   - Implementação de testes unitários com pytest
   - Geração de relatórios JUnit
   - Análise de cobertura de código
   - Estratégia de testes (passando e falhando)

3. **Containerização**:
   - Criação de Dockerfile
   - Build de imagens Docker
   - Deploy containerizado

4. **Boas Práticas**:
   - Versionamento de código (Git)
   - Documentação completa (README)
   - Estrutura de projeto organizada
   - Tratamento de erros

5. **Automação**:
   - Redução de trabalho manual
   - Feedback rápido sobre qualidade do código
   - Deploy automatizado

### Desafios Enfrentados

1. **Configuração Inicial do Jenkins**:
   - Instalação e configuração de plugins
   - Configuração de repositório Git
   - Ajustes de permissões

2. **Integração de Relatórios**:
   - Configuração de relatórios JUnit
   - Publicação de relatórios HTML
   - Formatação de saídas

3. **Compatibilidade de Ambientes**:
   - Diferenças entre Windows e Linux
   - Ajustes no Jenkinsfile para multiplataforma
   - Configuração de Docker

4. **Balanceamento de Testes**:
   - Criar testes que passam e falham
   - Demonstrar funcionalidades não implementadas
   - Manter pipeline funcional

### Melhorias Futuras

1. **Funcionalidades**:
   - Implementar campos de prioridade e data de vencimento
   - Adicionar paginação de resultados
   - Implementar atribuição de usuários
   - Adicionar autenticação e autorização

2. **Infraestrutura**:
   - Migrar de JSON para banco de dados (PostgreSQL/MySQL)
   - Implementar cache (Redis)
   - Adicionar load balancer

3. **Testes**:
   - Adicionar testes de integração
   - Implementar testes de performance
   - Adicionar testes end-to-end

4. **Documentação**:
   - Adicionar Swagger/OpenAPI
   - Criar documentação interativa
   - Adicionar exemplos de uso

5. **DevOps**:
   - Implementar deploy em múltiplos ambientes (dev, staging, prod)
   - Adicionar monitoramento (Prometheus, Grafana)
   - Implementar notificações (Slack, Teams)

### Impacto do Projeto

Este projeto demonstrou a importância de:
- **Automação**: Redução significativa de trabalho manual
- **Qualidade**: Garantia de qualidade através de testes automatizados
- **Rastreabilidade**: Histórico completo de builds e deploys
- **Colaboração**: Facilita trabalho em equipe com feedback rápido
- **Confiança**: Deploy automatizado reduz erros humanos

---

## 📚 Referências

- [Documentação Flask](https://flask.palletsprojects.com/)
- [Documentação pytest](https://docs.pytest.org/)
- [Documentação Jenkins](https://www.jenkins.io/doc/)
- [Documentação Docker](https://docs.docker.com/)
- [Best Practices CI/CD](https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/)

---

## 📎 Anexos

- [README.md](README.md) - Documentação completa do projeto
- [JENKINS_SETUP.md](JENKINS_SETUP.md) - Guia de configuração do Jenkins
- [GUIA_RAPIDO.md](GUIA_RAPIDO.md) - Guia rápido de uso
- [EXEMPLOS_API.md](EXEMPLOS_API.md) - Exemplos de uso da API
- [Jenkinsfile](Jenkinsfile) - Pipeline CI/CD completo

---

**Data de Entrega**: 16/12/2024  
**Versão**: 1.0.0

---

*Desenvolvido com ❤️ para demonstrar práticas de CI/CD com Jenkins*

