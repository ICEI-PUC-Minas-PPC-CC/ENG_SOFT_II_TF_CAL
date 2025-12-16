# 🔧 Como Instalar e Configurar Jenkins

Este guia mostra como instalar o Jenkins no Windows para executar o pipeline CI/CD.

---

## 📋 Opções de Instalação

Você tem 3 opções:

1. **Jenkins Local (Windows)** - Instalar no seu computador ⭐ Recomendado
2. **Jenkins em Nuvem** - Usar serviço online (mais fácil)
3. **Preparar para depois** - Código já está pronto, instale quando precisar

---

## 🖥️ Opção 1: Instalar Jenkins Localmente (Windows)

### Pré-requisitos

- Java JDK 11 ou superior instalado
- Windows 10/11

### Passo 1: Instalar Java JDK

1. **Verificar se Java já está instalado:**
   ```powershell
   java -version
   ```

2. **Se não estiver instalado:**
   - Baixe: https://adoptium.net/ (escolha JDK 11 ou 17)
   - Instale o arquivo `.msi`
   - Verifique novamente: `java -version`

### Passo 2: Baixar Jenkins

1. Acesse: https://www.jenkins.io/download/
2. Clique em **Windows** (versão LTS recomendada)
3. Baixe o arquivo `.msi`

### Passo 3: Instalar Jenkins

1. Execute o arquivo `.msi` baixado
2. Siga o assistente de instalação:
   - Aceite os termos
   - Escolha diretório de instalação (padrão OK)
   - Configure porta (padrão 8080 OK)
   - Instale como serviço Windows (recomendado)

### Passo 3.1: Configurar Credenciais do Serviço

Na tela **"Service Logon Credentials"**, você tem duas opções:

#### Opção A: LocalSystem (Mais Simples) ⭐ Recomendado para Iniciantes

1. Selecione: **"Run service as LocalSystem (not recommended)"**
   - ⚠️ Apesar de dizer "not recommended", é a opção mais simples para uso local/desenvolvimento
   - ✅ Não precisa de senha
   - ✅ Funciona imediatamente
   - ⚠️ Menos seguro (mas OK para uso local)

2. Clique em **Next** (não precisa testar credenciais)

#### Opção B: Usuário Local (Mais Seguro)

Se preferir usar um usuário específico:

1. Selecione: **"Run service as local or domain user:"**
2. Preencha:
   - **Account**: `.\SeuUsuario` ou `DOMINIO\Usuario`
     - Exemplo: `.\marce` (ponto e barra antes do nome)
     - Ou: `COMPUTADOR\marce`
   - **Password**: Sua senha do Windows
3. Clique em **Test Credentials**
4. Se aparecer "Credentials are valid", clique em **Next**
5. Se der erro, verifique:
   - Nome de usuário está correto?
   - Senha está correta?
   - Usuário tem permissões administrativas?

**💡 Dica**: Para uso local/testes, use **Opção A (LocalSystem)** - é mais fácil!

### Passo 4: Inicializar Jenkins

1. Abra o navegador: `http://localhost:8080`
2. Você verá uma tela pedindo senha inicial
3. **Encontrar senha inicial:**
   ```powershell
   type "C:\Program Files\Jenkins\secrets\initialAdminPassword"
   ```
   Ou procure no arquivo mostrado na tela

4. Cole a senha e clique em **Continue**

### Passo 5: Instalar Plugins

1. Escolha **"Install suggested plugins"** (recomendado)
2. Aguarde a instalação
3. Crie um usuário administrador
4. Configure URL (padrão OK)
5. Clique em **Save and Finish**

### Passo 6: Instalar Plugins Necessários

1. No Jenkins, vá em: **Manage Jenkins > Manage Plugins**
2. Na aba **Available**, instale:
   - ✅ **JUnit Plugin**
   - ✅ **HTML Publisher Plugin**
   - ✅ **Git Plugin**
   - ✅ **Pipeline Plugin** (geralmente já vem)

3. Clique em **Install without restart**
4. Aguarde e reinicie o Jenkins se necessário

### Passo 7: Configurar Job

Siga o guia [JENKINS_SETUP.md](JENKINS_SETUP.md) para configurar o pipeline.

---

## ☁️ Opção 2: Jenkins em Nuvem (Mais Fácil)

Se não quiser instalar localmente, use serviços online:

### Opção A: Jenkins X (Cloud)

- Acesse: https://jenkins-x.io/
- Crie conta gratuita
- Configure pipeline online

### Opção B: GitHub Actions (Alternativa)

Se você usar GitHub, pode usar GitHub Actions como alternativa ao Jenkins:

1. Crie arquivo `.github/workflows/ci.yml` no repositório
2. GitHub Actions executará o pipeline automaticamente

**Quer que eu crie um workflow do GitHub Actions para você?**

---

## ⏸️ Opção 3: Preparar para Depois

**Você não precisa instalar Jenkins agora!**

O código e pipeline já estão prontos:

- ✅ `Jenkinsfile` criado e configurado
- ✅ Testes funcionando
- ✅ Aplicação funcionando
- ✅ Documentação completa

**Quando precisar:**
1. Instale o Jenkins (seguindo este guia)
2. Configure o job (seguindo JENKINS_SETUP.md)
3. Execute o pipeline

---

## 🚀 Verificação Rápida

### Jenkins está rodando?

Abra no navegador: `http://localhost:8080`

- ✅ **Se abrir**: Jenkins está rodando!
- ❌ **Se não abrir**: Jenkins não está rodando

### Iniciar/Parar Jenkins

**Se instalou como serviço:**
```powershell
# Ver status
Get-Service Jenkins

# Iniciar
Start-Service Jenkins

# Parar
Stop-Service Jenkins
```

**Se instalou manualmente:**
```powershell
# Navegue até a pasta do Jenkins
cd "C:\Program Files\Jenkins"

# Iniciar
java -jar jenkins.war
```

---

## 🔍 Troubleshooting

### Problema: Porta 8080 já está em uso

**Solução:**
1. Altere a porta durante instalação (ex: 8081)
2. Ou pare o serviço usando a porta 8080

### Problema: Java não encontrado

**Solução:**
1. Instale Java JDK 11+ (veja Passo 1)
2. Adicione Java ao PATH do sistema
3. Reinicie o terminal

### Problema: Jenkins não inicia

**Solução:**
1. Verifique logs: `C:\Program Files\Jenkins\jenkins.err.log`
2. Verifique se Java está instalado: `java -version`
3. Verifique se a porta está livre

### Problema: Não consigo acessar http://localhost:8080

**Solução:**
1. Verifique se Jenkins está rodando (serviço Windows)
2. Verifique firewall (permita porta 8080)
3. Tente: `http://127.0.0.1:8080`

---

## 📝 Checklist de Instalação

- [ ] Java JDK instalado (`java -version`)
- [ ] Jenkins baixado e instalado
- [ ] Jenkins acessível em http://localhost:8080
- [ ] Senha inicial configurada
- [ ] Plugins instalados (JUnit, HTML Publisher, Git)
- [ ] Job criado e configurado
- [ ] Pipeline executando com sucesso

---

## 💡 Recomendação

**Para o trabalho final:**

1. **Se tiver tempo**: Instale Jenkins localmente (Opção 1)
2. **Se não tiver tempo**: Use GitHub Actions (Opção 2B) - posso criar o arquivo
3. **Se não precisar agora**: Deixe preparado para depois (Opção 3)

**O importante é que o código e pipeline já estão prontos!** ✅

---

## 🆘 Precisa de Ajuda?

- Consulte [JENKINS_SETUP.md](JENKINS_SETUP.md) para configurar o job
- Consulte [COMO_EXECUTAR.md](COMO_EXECUTAR.md) para executar localmente
- O código funciona sem Jenkins - você pode testar tudo localmente primeiro!

---

**Última atualização**: 2024

