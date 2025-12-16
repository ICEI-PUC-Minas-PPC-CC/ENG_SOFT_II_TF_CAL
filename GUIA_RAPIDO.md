# 🚀 Guia Rápido - Pipeline CI/CD Jenkins

## ⚡ Início Rápido

### 1. Executar Localmente

```bash
cd src
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### 2. Executar Testes

```bash
cd src
pytest tests/ -v
```

### 3. Configurar Jenkins

1. Instale plugins: JUnit, HTML Publisher, Git
2. Crie job tipo "Pipeline"
3. Configure: Pipeline script from SCM → Git → Jenkinsfile
4. Execute: "Build Now"

## 📋 Checklist de Entrega

- [ ] Repositório GitHub criado e código commitado
- [ ] Jenkinsfile configurado e funcionando
- [ ] Testes automatizados executando (10 passando, 6 falhando)
- [ ] Relatórios JUnit sendo gerados
- [ ] Relatório de cobertura disponível
- [ ] Artefatos sendo empacotados
- [ ] Deploy funcionando
- [ ] README completo com documentação
- [ ] Prints do pipeline no README ou documentação
- [ ] Casos de teste documentados

## 📸 O que Capturar (Prints)

1. **Pipeline Executando**: Tela do Jenkins mostrando stages em execução
2. **Test Results**: Página mostrando 10 testes passando e 6 falhando
3. **Cobertura de Código**: Relatório HTML de cobertura
4. **Artefatos**: Lista de arquivos empacotados
5. **Deploy**: Logs de deploy bem-sucedido
6. **Aplicação Funcionando**: Testes da API via curl ou Postman

## 🔗 Estrutura de Arquivos

```
├── Jenkinsfile          # Pipeline CI/CD
├── README.md            # Documentação principal
├── JENKINS_SETUP.md     # Guia de configuração
├── GUIA_RAPIDO.md       # Este arquivo
├── .gitignore
└── src/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── pytest.ini
    ├── tests/
    │   └── test_app.py
    ├── run_tests.sh
    └── run_tests.bat
```

## 🎯 Comandos Úteis

### Testar API Localmente

```bash
# Health check
curl http://localhost:5000/health

# Criar tarefa
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Teste", "status": "pendente"}'

# Listar tarefas
curl http://localhost:5000/tasks
```

### Gerar Relatório de Testes

```bash
cd src
pytest tests/ -v --junitxml=test-results.xml --cov=. --cov-report=html
```

## 📊 Métricas Esperadas

- **Total de Testes**: 16
- **Testes Passando**: 10
- **Testes Falhando**: 6 (intencionalmente)
- **Cobertura de Código**: ~70-80%

## ⚠️ Problemas Comuns

### Pipeline não encontra Python
- Instale Python no servidor Jenkins
- Ou use Docker

### Testes não geram relatório
- Verifique se `test-results.xml` está sendo criado
- Verifique permissões de escrita

### Docker não funciona
- Pipeline continua mesmo sem Docker
- Verifique se Docker está instalado e rodando

---

**Última atualização**: 2024

