# 🐳 Guia Rápido - Docker (Opcional)

## ⚠️ IMPORTANTE: Docker é OPCIONAL!

A aplicação funciona **perfeitamente sem Docker**. Use Docker apenas se quiser testar containerização.

---

## ❌ Erro que você está vendo:

```
error during connect: Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": 
open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```

**Causa**: Docker Desktop não está rodando.

---

## ✅ Solução 1: Iniciar Docker Desktop

### Passo 1: Abrir Docker Desktop

1. Pressione `Windows + S` (pesquisar)
2. Digite: **Docker Desktop**
3. Clique para abrir

### Passo 2: Aguardar Inicialização

- Aguarde até aparecer o ícone do Docker na **bandeja do sistema** (canto inferior direito)
- O ícone deve mostrar "Docker Desktop is running"

### Passo 3: Verificar se Funcionou

```powershell
docker ps
```

Se não der erro, está funcionando! ✅

### Passo 4: Executar Comandos Docker

```powershell
cd src
docker build -t todo-api .
docker run -d -p 5000:5000 --name todo-api todo-api
```

---

## ✅ Solução 2: Usar SEM Docker (Recomendado)

Você **NÃO precisa** de Docker para usar a aplicação!

### Executar Localmente (Mais Simples):

```powershell
# Terminal 1: Executar aplicação
cd src
python app.py

# Terminal 2: Testar API
cd src
.\test_api.ps1
```

**Pronto!** Aplicação funcionando sem Docker. ✅

---

## 🔍 Verificar Status do Docker

### Docker está rodando?

```powershell
docker ps
```

**Se funcionar**: Docker está OK ✅  
**Se der erro**: Docker não está rodando ❌

### Docker Desktop está instalado?

```powershell
docker --version
```

**Se mostrar versão**: Docker está instalado ✅  
**Se der erro**: Docker não está instalado ❌

---

## 📋 Checklist

- [ ] Docker Desktop instalado? (`docker --version`)
- [ ] Docker Desktop rodando? (ícone na bandeja do sistema)
- [ ] `docker ps` funciona sem erro?
- [ ] Se não, use a aplicação sem Docker (mais simples!)

---

## 💡 Recomendação

**Para o trabalho final, você pode:**
- ✅ Usar a aplicação localmente (Python)
- ✅ Executar testes localmente
- ✅ Configurar Jenkins (que funciona sem Docker)
- ✅ Docker é apenas um "bônus" se quiser testar

**O Jenkins continuará funcionando mesmo sem Docker!** O pipeline tem tratamento de erro para isso.

---

## 🆘 Ainda com Problemas?

1. **Docker não instalado?**
   - Baixe em: https://www.docker.com/products/docker-desktop
   - Ou simplesmente **não use Docker** - não é obrigatório!

2. **Docker não inicia?**
   - Reinicie o computador
   - Verifique se WSL2 está instalado (Windows)
   - Ou use sem Docker (mais fácil!)

3. **Quer continuar sem Docker?**
   - ✅ Perfeitamente OK!
   - ✅ Aplicação funciona normalmente
   - ✅ Testes funcionam normalmente
   - ✅ Jenkins funciona normalmente

---

**Lembre-se: Docker é OPCIONAL! Use apenas se quiser testar containerização.** 🚀

