# Guia de Configuração do Jenkins

Este documento contém instruções detalhadas para configurar o pipeline CI/CD no Jenkins.

## 📋 Pré-requisitos

### 1. Instalação do Jenkins

- Jenkins instalado e rodando
- Acesso administrativo ao Jenkins
- Java JDK instalado (requerido pelo Jenkins)

### 2. Plugins Necessários

Instale os seguintes plugins através do Jenkins:

1. **Pipeline** (já incluído)
2. **JUnit Plugin** - Para relatórios de testes
3. **HTML Publisher Plugin** - Para relatórios HTML de cobertura
4. **Git Plugin** - Para integração com Git
5. **Docker Pipeline** (opcional) - Se usar Docker
6. **Email Extension Plugin** (opcional) - Para notificações por email

**Como instalar plugins:**
1. Acesse: `Jenkins > Manage Jenkins > Manage Plugins`
2. Vá para a aba "Available"
3. Busque e marque os plugins
4. Clique em "Install without restart"

### 3. Configurações do Sistema

1. **Git**: Configure o Git no Jenkins (se necessário)
   - `Jenkins > Manage Jenkins > Global Tool Configuration`
   - Configure o caminho do Git

2. **Python** (se não usar Docker):
   - Certifique-se que Python 3.11+ está instalado no servidor Jenkins
   - Ou configure via "Global Tool Configuration"

## 🔧 Configuração do Job

### Passo 1: Criar Novo Job

1. Acesse o Jenkins
2. Clique em "New Item"
3. Digite um nome para o job (ex: `todo-api-pipeline`)
4. Selecione **"Pipeline"**
5. Clique em "OK"

### Passo 2: Configurar Pipeline

1. Na página de configuração do job, role até "Pipeline"
2. Em "Definition", selecione **"Pipeline script from SCM"**
3. Em "SCM", selecione **"Git"**
4. Configure:
   - **Repository URL**: URL do seu repositório GitHub
     - Exemplo: `https://github.com/seu-usuario/ENG_SOFT_II_TF_CAL.git`
   - **Credentials**: (se repositório privado) Configure credenciais do GitHub
   - **Branch Specifier**: `*/main` ou `*/master`
   - **Script Path**: `Jenkinsfile`

### Passo 3: Configurações Adicionais (Opcional)

1. **Build Triggers**:
   - Marque "GitHub hook trigger for GITScm polling" (se usar webhooks)
   - Ou configure "Poll SCM" para builds automáticos

2. **Post-build Actions**:
   - Já configurado no Jenkinsfile, mas pode adicionar aqui também

### Passo 4: Salvar

Clique em "Save" para salvar a configuração.

## 🚀 Executar o Pipeline

### Execução Manual

1. Acesse o job criado
2. Clique em **"Build Now"**
3. Acompanhe a execução em tempo real

### Execução Automática

O pipeline pode ser executado automaticamente quando:
- Há push no repositório (se webhook configurado)
- Há pull request (se configurado)
- Agendado via cron (se configurado)

## 📊 Visualizar Resultados

### Durante a Execução

1. Clique no build em execução
2. Clique em "Console Output" para ver logs em tempo real

### Após a Execução

1. **Status do Build**: Verde (sucesso), Vermelho (falha), Amarelo (instável)
2. **Test Result**: Clique para ver relatórios JUnit
3. **Relatório de Cobertura de Testes**: Clique para ver cobertura HTML
4. **Artifacts**: Baixe artefatos do build

## 🔍 Troubleshooting

### Problema: Pipeline não encontra o Jenkinsfile

**Solução**: Verifique se o `Jenkinsfile` está na raiz do repositório e o "Script Path" está correto.

### Problema: Erro ao instalar dependências Python

**Solução**: 
- Verifique se Python está instalado no servidor Jenkins
- Verifique se `pip` está disponível
- Adicione Python ao PATH do sistema

### Problema: Testes não geram relatório JUnit

**Solução**:
- Verifique se o arquivo `test-results.xml` está sendo gerado
- Verifique o caminho no Jenkinsfile: `junit 'src/test-results.xml'`
- Verifique permissões de escrita no diretório

### Problema: Docker não funciona

**Solução**:
- Verifique se Docker está instalado e rodando
- Verifique se o usuário do Jenkins tem permissão para usar Docker
- O pipeline continuará mesmo se Docker não estiver disponível (tratamento de erro implementado)

### Problema: Email não é enviado

**Solução**:
- Configure SMTP no Jenkins: `Manage Jenkins > Configure System > E-mail Notification`
- Ou desabilite emails no Jenkinsfile (comente as seções `emailext`)

## 📝 Personalizações

### Modificar Email de Notificação

No `Jenkinsfile`, altere:
```groovy
to: "${env.CHANGE_AUTHOR_EMAIL ?: 'seu-email@exemplo.com'}"
```

### Adicionar Mais Stages

Adicione novas stages no `Jenkinsfile`:
```groovy
stage('Nova Stage') {
    steps {
        echo 'Executando nova etapa...'
        // Seus comandos aqui
    }
}
```

### Modificar Porta da Aplicação

No `Dockerfile` e `app.py`, altere a porta de `5000` para a desejada.

## ✅ Checklist de Configuração

- [ ] Jenkins instalado e rodando
- [ ] Plugins necessários instalados
- [ ] Repositório Git configurado
- [ ] Job criado no Jenkins
- [ ] Pipeline configurado para usar Jenkinsfile
- [ ] Primeira execução bem-sucedida
- [ ] Relatórios de teste aparecendo
- [ ] Artefatos sendo gerados
- [ ] (Opcional) Docker funcionando
- [ ] (Opcional) Emails configurados

## 🎯 Próximos Passos

Após configurar o pipeline:

1. Teste diferentes cenários (push, pull request)
2. Configure webhooks do GitHub para builds automáticos
3. Adicione mais testes à aplicação
4. Implemente as funcionalidades que fazem os testes falharem
5. Configure deploy em ambiente de produção

---

**Última atualização**: 2024

