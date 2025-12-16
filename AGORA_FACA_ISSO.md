# ⚡ AGORA FAÇA ISSO - Guia Rápido

Você já configurou o Jenkins! Agora siga estes passos:

---

## 🎯 Passo 1: Criar Job no Jenkins (5 minutos)

1. **Abra o Jenkins**: http://localhost:8080
2. **Clique em**: "New Item" (ou "Novo Item")
3. **Digite um nome**: `todo-api-pipeline`
4. **Selecione**: "Pipeline"
5. **Clique em**: "OK"

---

## ⚙️ Passo 2: Configurar o Job (3 minutos)

Na página de configuração:

1. **Definition**: Selecione **"Pipeline script from SCM"**
2. **SCM**: Selecione **"Git"**
3. **Repository URL**: Cole a URL do seu repositório GitHub
   - Exemplo: `https://github.com/seu-usuario/ENG_SOFT_II_TF_CAL.git`
4. **Branch**: Digite `*/main` (ou `*/master`)
5. **Script Path**: Digite `Jenkinsfile`
6. **Clique em**: "Save"

---

## ▶️ Passo 3: Executar o Pipeline (10 minutos)

1. **Clique em**: "Build Now"
2. **Clique no build** #1 na lista
3. **Clique em**: "Console Output" para ver em tempo real
4. **AGUARDE** até terminar (pode levar 5-10 minutos)

---

## 📊 Passo 4: Ver Resultados (5 minutos)

Após terminar, você verá:

- 🟡 **Status AMARELO (Instável)** = ✅ **ISSO É NORMAL!** 
  - Significa que o pipeline funcionou, mas 6 testes falharam (isso é esperado!)

### Ver Relatórios:

1. **Clique em "Test Result"** → Veja os 16 testes (10 passando, 6 falhando)
2. **Procure por "Relatório de Cobertura de Testes"** → Clique para ver
3. **Procure por "Artifacts"** → Veja os arquivos gerados

---

## 📸 Passo 5: Tirar Prints (15 minutos)

Tire prints de:

1. ✅ Pipeline executando (Console Output)
2. ✅ Status final do build (mostrando as stages)
3. ✅ Test Result (10 passando, 6 falhando)
4. ✅ Relatório de Cobertura
5. ✅ Artefatos gerados

---

## 🚀 Passo 6: Testar Aplicação Localmente (10 minutos)

### Executar a API:

Abra um PowerShell na pasta `src`:

```powershell
cd C:\Users\marce\OneDrive\Documentos\Projetos\ENG_SOFT_II_TF_CAL\src
.\venv\Scripts\Activate.ps1
python app.py
```

### Testar a API:

Abra outro PowerShell e execute:

```powershell
cd C:\Users\marce\OneDrive\Documentos\Projetos\ENG_SOFT_II_TF_CAL\src
.\test_api.ps1
```

Ou teste manualmente no navegador/Postman:

- http://localhost:5000/health
- http://localhost:5000/

Tire prints das respostas!

---

## 📝 Passo 7: Finalizar Relatório (10 minutos)

1. **Abra**: `RELATORIO_FINAL.md`
2. **Preencha**: Nomes dos integrantes (linhas 11-16)
3. **Adicione**: Os prints que você tirou
4. **Preencha**: Informações no README.md também

---

## ✅ Checklist Rápido

- [ ] Job criado no Jenkins
- [ ] Pipeline executado
- [ ] Print do pipeline
- [ ] Print do Test Result
- [ ] Print do relatório de cobertura
- [ ] Aplicação testada localmente
- [ ] Prints da API funcionando
- [ ] RELATORIO_FINAL.md preenchido
- [ ] README.md com nomes dos integrantes

---

## ⏱️ Tempo Total Estimado: 1 hora

---

## 🆘 Se Algo Der Errado

### Pipeline falha?
- Veja os logs no "Console Output"
- Verifique se a URL do repositório está correta
- Verifique se o `Jenkinsfile` está na raiz do repositório

### Status amarelo (instável)?
- ✅ **ISSO É ESPERADO!** Temos 6 testes que falham intencionalmente
- O pipeline funcionou corretamente!

### Não consigo acessar o Jenkins?
- Verifique se está rodando: http://localhost:8080
- Reinicie o serviço Jenkins se necessário

---

## 📖 Documentação Completa

Para mais detalhes, consulte:
- `PROXIMOS_PASSOS.md` - Guia detalhado completo
- `JENKINS_SETUP.md` - Configuração do Jenkins
- `INSTALAR_JENKINS.md` - Instalação do Jenkins

---

**Boa sorte! 🚀**

