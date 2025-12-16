# 🔧 Troubleshooting - Testes Falhando

Se todos os testes estão falhando no Jenkins, siga este guia para diagnosticar e resolver.

---

## ✅ O Que Foi Corrigido

Atualizei o `Jenkinsfile` para funcionar corretamente no Windows:

1. ✅ Uso de `bat` em vez de `sh` para comandos Windows
2. ✅ Ativação correta do ambiente virtual no Windows
3. ✅ Correção de caminhos (usando `\\` em vez de `/` no Windows)
4. ✅ Comandos específicos para cada sistema operacional

---

## 🔍 Passo 1: Verificar os Logs do Jenkins

1. No Jenkins, vá até o build que falhou
2. Clique em **"Console Output"** (ou "Saída do Console")
3. Role até a seção **"Test"**
4. Procure por erros como:
   - `ModuleNotFoundError`
   - `No module named 'app'`
   - `pytest: command not found`
   - `ImportError`

### Exemplo de Erros Comuns:

#### Erro 1: "ModuleNotFoundError: No module named 'app'"
```
E   ModuleNotFoundError: No module named 'app'
```

**Solução**: O Python não está encontrando o módulo. Isso foi corrigido no Jenkinsfile atualizado.

#### Erro 2: "pytest: command not found"
```
pytest: command not found
```

**Solução**: As dependências não foram instaladas. Verifique se o stage "Build" foi executado com sucesso.

#### Erro 3: "ImportError"
```
ImportError: cannot import name 'app' from 'app'
```

**Solução**: Problema de caminho ou o arquivo app.py não está no diretório correto.

---

## 🔍 Passo 2: Testar Localmente

Antes de rodar no Jenkins, teste localmente para garantir que funciona:

### No PowerShell:

```powershell
cd C:\Users\marce\OneDrive\Documentos\Projetos\ENG_SOFT_II_TF_CAL\src

# Ativa ambiente virtual
.\venv\Scripts\Activate.ps1

# Instala dependências (se necessário)
pip install -r requirements.txt

# Executa os testes
pytest tests/ -v --junitxml=test-results.xml
```

**Resultado esperado**: 10 testes passando, 6 falhando

Se funcionar localmente mas falhar no Jenkins, o problema é no Jenkinsfile.

---

## 🔍 Passo 3: Verificar o Stage "Build"

No Console Output, procure pela seção **"Build"**:

```
[Pipeline] { (Build)
[Pipeline] echo
Construindo a aplicação...
[Pipeline] dir
Running in C:\Users\...\workspace\...\src
[Pipeline] {
[Pipeline] bat
...
```

Verifique se:
- ✅ O ambiente virtual foi criado (`venv` folder)
- ✅ O pip foi atualizado
- ✅ As dependências foram instaladas (`pip install -r requirements.txt`)
- ✅ Não há erros de instalação

---

## 🔍 Passo 4: Verificar o Stage "Test"

No Console Output, procure pela seção **"Test"**:

```
[Pipeline] { (Test)
[Pipeline] echo
Executando testes automatizados...
[Pipeline] dir
Running in C:\Users\...\workspace\...\src
[Pipeline] {
[Pipeline] bat
...
```

Verifique:
- ✅ O ambiente virtual está sendo ativado (`call venv\Scripts\activate.bat`)
- ✅ O pytest está sendo executado
- ✅ Os testes estão sendo encontrados

---

## 🛠️ Soluções por Problema

### Problema: "pytest não encontrado"

**Solução 1**: Verifique se o requirements.txt está sendo instalado:
```groovy
// No Jenkinsfile, stage Build deve ter:
pip install -r requirements.txt
```

**Solução 2**: Instale manualmente no ambiente virtual:
```powershell
.\venv\Scripts\Activate.ps1
pip install pytest pytest-cov
```

### Problema: "No module named 'app'"

**Solução**: O problema é o caminho. Certifique-se de que:
1. Os testes estão rodando no diretório `src/`
2. O arquivo `app.py` está em `src/app.py`
3. O arquivo `tests/test_app.py` tem o import correto

### Problema: "ImportError: cannot import name 'app'"

**Solução**: Verifique se o `src/tests/test_app.py` tem:
```python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, DATA_FILE
```

---

## 📋 Checklist de Verificação

Execute este checklist no Jenkins:

- [ ] Stage "Build" executou sem erros
- [ ] Ambiente virtual foi criado (`venv` folder existe)
- [ ] Dependências foram instaladas (veja nos logs)
- [ ] Stage "Test" está usando o Python do venv
- [ ] Pytest está instalado e funcionando
- [ ] Arquivo `test-results.xml` está sendo gerado
- [ ] Erros específicos aparecem nos logs

---

## 🔄 Como Re-executar

Após corrigir o Jenkinsfile:

1. **Faça commit das alterações**:
   ```powershell
   git add Jenkinsfile
   git commit -m "Fix: Corrigir Jenkinsfile para Windows"
   git push
   ```

2. **No Jenkins**:
   - Vá até o job
   - Clique em **"Build Now"** novamente
   - Acompanhe os logs

3. **Verifique os resultados**:
   - Deve ter 10 testes passando
   - Deve ter 6 testes falhando (intencionalmente)

---

## 🆘 Se Ainda Não Funcionar

### Opção 1: Executar Testes Manualmente no Jenkins

Você pode executar os testes manualmente no servidor Jenkins:

1. Conecte-se ao servidor Jenkins (ou use o próprio servidor onde está)
2. Navegue até o workspace do job:
   ```
   C:\Users\<usuario>\.jenkins\workspace\<nome-do-job>\src
   ```
3. Execute os testes manualmente para ver o erro real

### Opção 2: Usar PowerShell Script

Crie um script PowerShell para executar os testes e veja o erro:

```powershell
# test_manual.ps1
cd src
.\venv\Scripts\Activate.ps1
pytest tests/ -v
```

Execute este script e veja qual é o erro exato.

### Opção 3: Verificar Versão do Python

No Jenkinsfile, você pode adicionar um comando para verificar a versão:

```groovy
stage('Build') {
    steps {
        dir('src') {
            bat '''
                python --version
                python -m venv venv
                call venv\\Scripts\\activate.bat
                python --version
                pip --version
            '''
        }
    }
}
```

---

## 📞 Informações para Debug

Se precisar de ajuda, forneça:

1. **Logs completos** do Console Output (especialmente a parte do Test)
2. **Versão do Python** no servidor Jenkins
3. **Sistema operacional** do servidor Jenkins
4. **Mensagens de erro** específicas
5. **Resultado dos testes locais** (funciona localmente?)

---

## ✅ Resultado Esperado

Após corrigir, você deve ver:

```
tests/test_app.py::test_health_check PASSED
tests/test_app.py::test_index_endpoint PASSED
tests/test_app.py::test_create_task_success PASSED
tests/test_app.py::test_get_all_tasks PASSED
tests/test_app.py::test_get_task_by_id PASSED
tests/test_app.py::test_update_task_success PASSED
tests/test_app.py::test_delete_task_success PASSED
tests/test_app.py::test_filter_tasks_by_status PASSED
tests/test_app.py::test_create_task_without_title_fails PASSED
tests/test_app.py::test_task_has_priority_field FAILED  ← Intencional
tests/test_app.py::test_task_has_due_date FAILED  ← Intencional
tests/test_app.py::test_update_nonexistent_task_returns_error FAILED  ← Intencional
tests/test_app.py::test_task_auto_assigns_user FAILED  ← Intencional
tests/test_app.py::test_get_tasks_with_pagination FAILED  ← Intencional
tests/test_app.py::test_task_status_validation FAILED  ← Intencional

========== 10 passed, 6 failed in X.XXs ==========
```

---

**Última atualização**: 2024  
**Status do Jenkinsfile**: ✅ Corrigido para Windows

