# 🚀 Próximos Passos - Após Configurar Jenkins

Agora que o Jenkins está configurado, siga estes passos para executar o pipeline e finalizar o projeto.

---

## ✅ Passo 1: Verificar se Jenkins Está Rodando

1. **Abra o navegador** e acesse:
   ```
   http://localhost:8080
   ```

2. **Faça login** no Jenkins (com as credenciais que você criou)

3. Se a página do Jenkins abrir, está tudo certo! ✅

---

## 🔧 Passo 2: Criar o Job no Jenkins

### 2.1. Criar Novo Job

1. No Jenkins, clique em **"New Item"** (ou "Novo Item")
2. Digite um nome para o job:
   - Exemplo: `todo-api-pipeline` ou `eng-soft-ii-tf-cal`
3. Selecione **"Pipeline"**
4. Clique em **"OK"**

### 2.2. Configurar o Pipeline

Na página de configuração, role até a seção **"Pipeline"**:

1. **Definition**: Selecione **"Pipeline script from SCM"**
2. **SCM**: Selecione **"Git"**
3. **Repository URL**: Cole a URL do seu repositório GitHub
   - Exemplo: `https://github.com/seu-usuario/ENG_SOFT_II_TF_CAL.git`
   - Ou: `git@github.com:seu-usuario/ENG_SOFT_II_TF_CAL.git`
4. **Credentials**: 
   - Se o repositório é **público**: Deixe em branco
   - Se é **privado**: Clique em "Add" e configure suas credenciais do GitHub
5. **Branch Specifier**: Digite `*/main` (ou `*/master` se for master)
6. **Script Path**: Digite `Jenkinsfile` (deve estar na raiz do repositório)

### 2.3. Salvar Configuração

1. Clique em **"Save"** (ou "Salvar")
2. Você será redirecionado para a página do job

---

## 🎬 Passo 3: Executar o Pipeline

### 3.1. Execução Manual (Primeira Vez)

1. Na página do job, clique em **"Build Now"** (ou "Construir Agora")
2. Você verá um novo build na lista (Build #1)
3. Clique no build para ver os detalhes
4. Clique em **"Console Output"** para ver os logs em tempo real

### 3.2. Acompanhar Execução

O pipeline passará pelas seguintes stages:

1. ✅ **Checkout** - Fazendo checkout do código...
2. ✅ **Build** - Construindo a aplicação...
3. ✅ **Test** - Executando testes automatizados...
4. ✅ **Quality Check** - Verificando qualidade do código...
5. ✅ **Package** - Empacotando artefatos...
6. ✅ **Docker Build** - Construindo imagem Docker... (pode pular se Docker não estiver disponível)
7. ✅ **Deploy** - Realizando deploy...

**Aguarde a execução terminar** (pode levar alguns minutos na primeira vez)

---

## 📊 Passo 4: Verificar Resultados

### 4.1. Status do Build

Após a execução, você verá um dos seguintes status:

- 🟢 **Sucesso** (azul/verde) - Tudo funcionou!
- 🟡 **Instável** (amarelo) - Pipeline executou, mas alguns testes falharam (esperado!)
- 🔴 **Falha** (vermelho) - Algo deu errado

**Nota**: É **NORMAL** que o pipeline fique **INSTÁVEL** (amarelo) porque temos 6 testes que falham intencionalmente!

### 4.2. Visualizar Relatórios

Na página do build, você encontrará:

#### 📋 Relatórios de Teste (JUnit)

1. Clique em **"Test Result"** (ou "Resultado do Teste")
2. Você verá:
   - Total de testes: 16
   - Testes passando: 10 ✅
   - Testes falhando: 6 ❌
3. **IMPORTANTE**: Tire um print desta tela!

#### 📈 Relatório de Cobertura

1. Role a página do build até encontrar **"Relatório de Cobertura de Testes"**
2. Clique para ver o relatório HTML
3. **IMPORTANTE**: Tire um print desta tela!

#### 📦 Artefatos

1. Na página do build, procure por **"Artifacts"**
2. Você verá os arquivos empacotados
3. **IMPORTANTE**: Tire um print desta tela!

---

## 📸 Passo 5: Tirar Prints Necessários

### 5.1. Prints do Pipeline

Tire prints das seguintes telas:

1. **Pipeline em execução** (com todas as stages)
   - Vá em "Console Output" durante a execução
   
2. **Status final do build**
   - Mostrando sucesso/instável com todas as stages

3. **Relatório JUnit**
   - Mostrando 10 testes passando e 6 falhando
   - Clique em "Test Result" para ver detalhes

4. **Relatório de Cobertura**
   - Clique em "Relatório de Cobertura de Testes"

5. **Artefatos gerados**
   - Mostrando arquivos empacotados

### 5.2. Prints da Aplicação

Antes de tirar prints da aplicação, você precisa executá-la:

#### Executar a Aplicação Localmente

```powershell
# No PowerShell, navegue até a pasta do projeto
cd C:\Users\marce\OneDrive\Documentos\Projetos\ENG_SOFT_II_TF_CAL\src

# Ative o ambiente virtual
.\venv\Scripts\Activate.ps1

# Execute a aplicação
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

#### Testar e Tirar Prints

Use **Postman** ou **curl** para testar:

1. **Health Check**
   ```
   GET http://localhost:5000/health
   ```
   - Tire print da resposta

2. **Criar Tarefa**
   ```
   POST http://localhost:5000/tasks
   Body (JSON):
   {
     "title": "Teste de Tarefa",
     "description": "Descrição da tarefa",
     "status": "pendente"
   }
   ```
   - Tire print da requisição e resposta

3. **Listar Tarefas**
   ```
   GET http://localhost:5000/tasks
   ```
   - Tire print da resposta

4. **Buscar Tarefa por ID**
   ```
   GET http://localhost:5000/tasks/1
   ```
   - Tire print da resposta

5. **Atualizar Tarefa**
   ```
   PUT http://localhost:5000/tasks/1
   Body (JSON):
   {
     "title": "Tarefa Atualizada",
     "status": "concluida"
   }
   ```
   - Tire print da requisição e resposta

---

## 📝 Passo 6: Adicionar Prints ao Relatório Final

1. Abra o arquivo `RELATORIO_FINAL.md`

2. Substitua os placeholders de imagens pelos prints que você tirou:
   - Exemplo: `![Pipeline Executando](imagens/pipeline-executando.png)`
   - Adicione as imagens em uma pasta `imagens/` ou use links do GitHub

3. Preencha a seção **"Identificação dos Integrantes"** com os nomes reais

---

## ✅ Passo 7: Checklist Final

Verifique se você tem:

- [ ] Pipeline executado no Jenkins
- [ ] Print do pipeline em execução
- [ ] Print do status final (instável é OK!)
- [ ] Print do relatório JUnit (10 passando, 6 falhando)
- [ ] Print do relatório de cobertura
- [ ] Print dos artefatos
- [ ] Aplicação executada localmente
- [ ] Prints dos endpoints da API funcionando
- [ ] RELATORIO_FINAL.md preenchido com prints e informações dos integrantes
- [ ] README.md preenchido com informações dos integrantes

---

## 🆘 Problemas Comuns e Soluções

### Problema: Pipeline falha no Checkout

**Solução:**
- Verifique se a URL do repositório está correta
- Se o repositório for privado, configure as credenciais
- Verifique se o branch está correto (main/master)

### Problema: Pipeline falha no Build

**Solução:**
- Verifique se Python está instalado no servidor Jenkins
- Verifique se o caminho do Python está correto
- Windows: pode precisar usar `python` em vez de `python3`

### Problema: Testes não geram relatório

**Solução:**
- Verifique se o arquivo `test-results.xml` está sendo gerado
- Verifique permissões de escrita no diretório
- Veja os logs do Console Output para erros

### Problema: Docker não funciona

**Solução:**
- Isso é **OK**! O pipeline continua mesmo sem Docker
- Você verá uma mensagem "Docker não disponível, pulando etapa"
- O pipeline continuará normalmente

### Problema: Pipeline fica instável (amarelo)

**Solução:**
- Isso é **ESPERADO**! Temos 6 testes que falham intencionalmente
- O status instável significa: pipeline executou, mas alguns testes falharam
- Isso demonstra que o pipeline está funcionando corretamente
- Você pode considerar isso como sucesso parcial

---

## 🎯 Resumo dos Próximos Passos

1. ✅ Criar job no Jenkins (Passo 2)
2. ✅ Executar pipeline (Passo 3)
3. ✅ Verificar resultados (Passo 4)
4. ✅ Tirar prints (Passo 5)
5. ✅ Executar aplicação e testar (Passo 5.2)
6. ✅ Adicionar prints ao relatório (Passo 6)
7. ✅ Preencher informações dos integrantes
8. ✅ Revisar tudo
9. ✅ Fazer commit final
10. ✅ Entregar no Classroom

---

## 📞 Precisa de Ajuda?

Se encontrar problemas:

1. Veja os logs no "Console Output" do build
2. Consulte `JENKINS_SETUP.md` para configurações
3. Consulte `INSTALAR_JENKINS.md` para problemas de instalação
4. Verifique se todos os plugins estão instalados

---

**Boa sorte com a execução! 🚀**

