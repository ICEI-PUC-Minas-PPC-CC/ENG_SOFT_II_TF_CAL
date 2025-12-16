# 🚀 Como Executar a Aplicação

Este guia contém instruções passo a passo para executar a aplicação localmente e configurar o pipeline no Jenkins.

> **💡 DICAS**: 
> - Docker é **OPCIONAL**! Veja [DOCKER_GUIA_RAPIDO.md](DOCKER_GUIA_RAPIDO.md)
> - **Não tem Jenkins?** Veja [INSTALAR_JENKINS.md](INSTALAR_JENKINS.md) ou use GitHub Actions (já configurado!)

---

## 📋 Índice

1. [Execução Local (Desenvolvimento)](#execução-local) ⭐ **RECOMENDADO**
2. [Executar Testes](#executar-testes)
3. [Executar com Docker](#executar-com-docker) (Opcional)
4. [Configurar Jenkins](#configurar-jenkins) - Veja [INSTALAR_JENKINS.md](INSTALAR_JENKINS.md) primeiro!
5. [GitHub Actions (Alternativa ao Jenkins)](#github-actions)
6. [Troubleshooting](#troubleshooting)

---

## 🖥️ Execução Local

### Pré-requisitos

- Python 3.11 ou superior instalado
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

### Passo 1: Clonar o Repositório

```bash
git clone <url-do-seu-repositorio>
cd ENG_SOFT_II_TF_CAL
```

### Passo 2: Navegar para o Diretório src

```bash
cd src
```

### Passo 3: Criar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Você verá `(venv)` no início da linha do terminal quando o ambiente estiver ativo.

### Passo 4: Instalar Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 5: Executar a Aplicação

```bash
python app.py
```

Você verá uma saída similar a:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[seu-ip]:5000
Press CTRL+C to quit
```

### Passo 6: Testar a API

Abra um **novo terminal** (mantenha o servidor rodando) e teste:

#### Opção A: Usando curl (Linux/Mac ou Git Bash no Windows)

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Criar uma tarefa:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Minha primeira tarefa\", \"status\": \"pendente\"}"
```

**Listar tarefas:**
```bash
curl http://localhost:5000/tasks
```

#### Opção B: Usando PowerShell (Windows) - RECOMENDADO

**Health Check:**
```powershell
Invoke-RestMethod -Uri http://localhost:5000/health -Method Get
```

**Criar uma tarefa:**
```powershell
$body = @{
    title = "Minha primeira tarefa"
    status = "pendente"
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5000/tasks -Method Post -Body $body -ContentType "application/json"
```

**Listar tarefas:**
```powershell
Invoke-RestMethod -Uri http://localhost:5000/tasks -Method Get
```

**Atualizar tarefa:**
```powershell
$body = @{
    title = "Tarefa atualizada"
    status = "concluida"
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5000/tasks/1 -Method Put -Body $body -ContentType "application/json"
```

**Remover tarefa:**
```powershell
Invoke-RestMethod -Uri http://localhost:5000/tasks/1 -Method Delete
```

#### Opção C: Usando Script PowerShell (Mais Fácil)

Crie um arquivo `test_api.ps1` no diretório `src`:

```powershell
# Health Check
Write-Host "`n🔍 Health Check:" -ForegroundColor Cyan
Invoke-RestMethod -Uri http://localhost:5000/health -Method Get | ConvertTo-Json

# Criar tarefa
Write-Host "`n➕ Criando tarefa..." -ForegroundColor Cyan
$body = @{title="Teste API"; status="pendente"} | ConvertTo-Json
$task = Invoke-RestMethod -Uri http://localhost:5000/tasks -Method Post -Body $body -ContentType "application/json"
Write-Host "Tarefa criada:" -ForegroundColor Green
$task | ConvertTo-Json

# Listar tarefas
Write-Host "`n📋 Listando todas as tarefas:" -ForegroundColor Cyan
$tasks = Invoke-RestMethod -Uri http://localhost:5000/tasks -Method Get
$tasks | ConvertTo-Json -Depth 10
```

Execute com:
```powershell
.\test_api.ps1
```

### Parar a Aplicação

No terminal onde a aplicação está rodando, pressione `CTRL+C`.

---

## 🧪 Executar Testes

### Opção 1: Usando Scripts (Recomendado)

**Windows (PowerShell):**
```powershell
cd src
.\run_tests.bat
```

**Windows (CMD):**
```cmd
cd src
run_tests.bat
```

**Linux/Mac:**
```bash
cd src
chmod +x run_tests.sh
./run_tests.sh
```

**Windows (PowerShell - Script nativo):**
```powershell
cd src
.\run_tests.ps1
```

### Opção 2: Comando Manual

Certifique-se de estar no diretório `src` e com o ambiente virtual ativado:

```bash
# Executar todos os testes
pytest tests/ -v

# Executar com cobertura
pytest tests/ -v --cov=. --cov-report=html --cov-report=term-missing

# Executar e gerar relatório JUnit (para Jenkins)
pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
```

### Visualizar Relatório de Cobertura

Após executar com `--cov-report=html`, abra no navegador:

```
src/htmlcov/index.html
```

---

## 🐳 Executar com Docker

> **⚠️ IMPORTANTE**: Docker é **OPCIONAL**. A aplicação funciona perfeitamente sem Docker usando apenas Python. Use Docker apenas se quiser testar a containerização.

### Pré-requisitos

- Docker Desktop instalado
- Docker Desktop **rodando** (verifique o ícone na bandeja do sistema)

### Verificar se Docker está Rodando

**Windows:**
```powershell
docker --version
docker ps
```

Se aparecer erro como `The system cannot find the file specified` ou `Cannot connect to the Docker daemon`, o Docker Desktop não está rodando.

**Solução:**
1. Abra o **Docker Desktop** (procure no menu Iniciar)
2. Aguarde até aparecer "Docker Desktop is running" na bandeja do sistema
3. Tente novamente: `docker ps`

### Passo 1: Construir a Imagem

```bash
cd src
docker build -t todo-api .
```

**Se der erro**, verifique:
- Docker Desktop está rodando?
- Você está no diretório `src`?
- O arquivo `Dockerfile` existe em `src/`?

### Passo 2: Executar o Container

```bash
docker run -d -p 5000:5000 --name todo-api todo-api
```

### Passo 3: Testar

**PowerShell:**
```powershell
Invoke-RestMethod -Uri http://localhost:5000/health -Method Get
```

**Linux/Mac:**
```bash
curl http://localhost:5000/health
```

### Passo 4: Ver Logs

```bash
docker logs todo-api
```

### Passo 5: Parar e Remover Container

```bash
docker stop todo-api
docker rm todo-api
```

### Docker não Funciona? Sem Problema!

Se você não conseguir usar Docker ou não quiser instalar:
- ✅ A aplicação funciona **perfeitamente sem Docker**
- ✅ Use a execução local com Python (veja seção "Execução Local")
- ✅ O Jenkins continuará funcionando mesmo sem Docker (tratamento de erro implementado)

---

## 🔧 Configurar Jenkins

> **⚠️ Não tem Jenkins instalado?** 
> - Veja [INSTALAR_JENKINS.md](INSTALAR_JENKINS.md) para instalar primeiro
> - Ou use [GitHub Actions](#github-actions) como alternativa (mais fácil e já configurado!)

### Pré-requisitos

- Jenkins instalado e rodando (veja [INSTALAR_JENKINS.md](INSTALAR_JENKINS.md))
- Jenkins acessível em `http://localhost:8080`

### Passo 1: Instalar Plugins

1. Acesse o Jenkins: `http://localhost:8080` (ou URL do seu Jenkins)
2. Vá em: **Manage Jenkins > Manage Plugins**
3. Na aba **Available**, instale:
   - ✅ JUnit Plugin
   - ✅ HTML Publisher Plugin
   - ✅ Git Plugin
   - ✅ Pipeline Plugin (geralmente já vem instalado)

### Passo 2: Criar Novo Job

1. Clique em **New Item**
2. Digite o nome: `todo-api-pipeline`
3. Selecione **Pipeline**
4. Clique em **OK**

### Passo 3: Configurar Pipeline

1. Role até a seção **Pipeline**
2. Em **Definition**, selecione: **Pipeline script from SCM**
3. Em **SCM**, selecione: **Git**
4. Configure:
   - **Repository URL**: `https://github.com/seu-usuario/ENG_SOFT_II_TF_CAL.git`
   - **Branch**: `*/main` ou `*/master`
   - **Script Path**: `Jenkinsfile`
5. Clique em **Save**

### Passo 4: Executar Pipeline

1. Clique em **Build Now**
2. Acompanhe a execução clicando no build e depois em **Console Output**

### Passo 5: Ver Resultados

Após a execução, você verá:

- ✅ **Status**: Verde (sucesso), Amarelo (instável), Vermelho (falha)
- 📊 **Test Result**: Clique para ver relatórios JUnit
- 📈 **Relatório de Cobertura**: Clique para ver cobertura HTML
- 📦 **Artifacts**: Baixe artefatos do build

---

## 🐙 GitHub Actions (Alternativa ao Jenkins)

Se você não tem Jenkins ou prefere uma solução mais simples, use **GitHub Actions**!

### Vantagens

- ✅ Não precisa instalar nada
- ✅ Executa automaticamente no GitHub
- ✅ Grátis para repositórios públicos
- ✅ Já configurado! (arquivo `.github/workflows/ci.yml`)

### Como Usar

1. **Faça push do código para GitHub:**
   ```powershell
   git add .
   git commit -m "Adiciona pipeline CI/CD"
   git push origin main
   ```

2. **Acesse seu repositório no GitHub**

3. **Vá em "Actions"** (aba no topo)

4. **Veja o pipeline executando automaticamente!**

5. **Visualize resultados:**
   - Testes passando/falhando
   - Cobertura de código
   - Artefatos gerados

### Configuração

O arquivo `.github/workflows/ci.yml` já está criado e configurado!

**Funcionalidades:**
- ✅ Executa testes automaticamente
- ✅ Gera relatórios JUnit
- ✅ Calcula cobertura de código
- ✅ Publica resultados
- ✅ Build Docker (opcional)

### Comparação: Jenkins vs GitHub Actions

| Recurso | Jenkins | GitHub Actions |
|---------|---------|---------------|
| Instalação | Requer instalação local | Já no GitHub |
| Configuração | Manual | Automática |
| Custo | Grátis | Grátis (público) |
| Execução | Manual ou agendada | Automática (push/PR) |
| Interface | Web local | Web no GitHub |

**Recomendação**: Use GitHub Actions se não quiser instalar Jenkins!

---

## 🔍 Verificar se Está Funcionando

### Teste 1: API Respondendo

**Linux/Mac/Git Bash:**
```bash
curl http://localhost:5000/health
```

**PowerShell (Windows):**
```powershell
Invoke-RestMethod -Uri http://localhost:5000/health -Method Get
```

**Resposta esperada:**
```json
{
  "status": "healthy",
  "timestamp": "2024-12-16T..."
}
```

### Teste 2: Criar e Listar Tarefas

**Linux/Mac/Git Bash:**
```bash
# Criar
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Teste\", \"status\": \"pendente\"}"

# Listar
curl http://localhost:5000/tasks
```

**PowerShell (Windows):**
```powershell
# Criar
$body = @{title="Teste"; status="pendente"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/tasks -Method Post -Body $body -ContentType "application/json"

# Listar
Invoke-RestMethod -Uri http://localhost:5000/tasks -Method Get
```

### Teste 3: Testes Passando

```bash
cd src
pytest tests/ -v
```

**Resultado esperado:**
- 10 testes passando ✅
- 6 testes falhando ❌ (intencionalmente)

---

## ⚠️ Troubleshooting

### Problema: "python não é reconhecido como comando"

**Solução:**
- Windows: Use `py` ou `python3` em vez de `python`
- Verifique se Python está no PATH do sistema
- Reinstale Python marcando "Add Python to PATH"

### Problema: "pip não encontrado"

**Solução:**
```bash
python -m ensurepip --upgrade
# ou
python3 -m ensurepip --upgrade
```

### Problema: "ModuleNotFoundError: No module named 'flask'"

**Solução:**
```bash
# Certifique-se de que o ambiente virtual está ativado
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

pip install -r requirements.txt
```

### Problema: "Port 5000 already in use"

**Solução:**
- Pare outros processos usando a porta 5000
- Ou altere a porta no `app.py`:
  ```python
  app.run(host='0.0.0.0', port=5001, debug=True)
  ```

### Problema: PowerShell não executa scripts (.ps1)

**Solução:**
- Execute no PowerShell:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- Ou execute scripts com:
  ```powershell
  .\nome_do_script.ps1
  ```

### Problema: "run_tests.bat não é reconhecido" no PowerShell

**Solução:**
- No PowerShell, use `.\` antes do nome do arquivo:
  ```powershell
  .\run_tests.bat
  ```
- Ou use o script PowerShell nativo:
  ```powershell
  .\run_tests.ps1
  ```

### Problema: Jenkins não encontra o Jenkinsfile

**Solução:**
- Verifique se o `Jenkinsfile` está na raiz do repositório
- Verifique se o "Script Path" está configurado como `Jenkinsfile`
- Verifique se o repositório foi clonado corretamente

### Problema: Testes não geram relatório JUnit

**Solução:**
```bash
# Execute com a flag --junitxml
pytest tests/ -v --junitxml=test-results.xml
```

### Problema: Docker não funciona / "The system cannot find the file specified"

**Solução:**
1. **Verifique se Docker Desktop está instalado:**
   ```powershell
   docker --version
   ```

2. **Inicie o Docker Desktop:**
   - Abra o menu Iniciar
   - Procure "Docker Desktop"
   - Aguarde até aparecer "Docker Desktop is running" na bandeja do sistema

3. **Verifique se está rodando:**
   ```powershell
   docker ps
   ```
   Se funcionar, o Docker está OK.

4. **Docker não é obrigatório:**
   - ✅ A aplicação funciona perfeitamente sem Docker
   - ✅ Use a execução local com Python
   - ✅ O Jenkins continuará funcionando mesmo sem Docker

### Problema: Docker não funciona no Jenkins

**Solução:**
- O pipeline continuará mesmo sem Docker (tratamento de erro implementado)
- Para usar Docker, certifique-se de que:
  - Docker está instalado no servidor Jenkins
  - Usuário do Jenkins tem permissão para usar Docker
  - Docker está rodando: `sudo systemctl status docker` (Linux) ou Docker Desktop rodando (Windows)

---

## 📝 Checklist de Execução

### Execução Local
- [ ] Python 3.11+ instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas
- [ ] Aplicação rodando em http://localhost:5000
- [ ] Health check respondendo
- [ ] Testes executando (10 passando, 6 falhando)
- [ ] (Opcional) Docker funcionando

### Jenkins
- [ ] Jenkins instalado e rodando
- [ ] Plugins instalados (JUnit, HTML Publisher, Git)
- [ ] Job criado e configurado
- [ ] Pipeline executando com sucesso
- [ ] Relatórios JUnit aparecendo
- [ ] Relatório de cobertura disponível
- [ ] Artefatos sendo gerados

---

## 🎯 Próximos Passos

Após conseguir executar localmente:

1. ✅ Teste todos os endpoints da API
2. ✅ Execute os testes e verifique os resultados
3. ✅ Configure o Jenkins seguindo os passos acima
4. ✅ Execute o pipeline no Jenkins
5. ✅ Capture prints para documentação
6. ✅ Preencha o `RELATORIO_FINAL.md` com os resultados

---

## 📞 Precisa de Ajuda?

- Consulte o [README.md](README.md) para documentação completa
- Consulte o [JENKINS_SETUP.md](JENKINS_SETUP.md) para detalhes do Jenkins
- Consulte o [EXEMPLOS_API.md](EXEMPLOS_API.md) para mais exemplos de uso

---

**Última atualização**: 2024

