# 🔍 Diagnosticar Falha no Pipeline

O pipeline falhou antes do Deploy. Precisamos ver qual stage falhou.

---

## 📋 O que Preciso Ver

No Console Output do Jenkins, procure pela seção que mostra o **erro real**. 

Provavelmente está em uma dessas sections:

### 1. Seção "Test" (mais provável)

Procure por algo assim:

```
[Pipeline] { (Test)
[Pipeline] echo
Executando testes automatizados...
[Pipeline] dir
...
[Pipeline] bat
...
```

**Me envie esta parte completa!**

### 2. Seção "Build"

```
[Pipeline] { (Build)
[Pipeline] echo
Construindo a aplicação...
...
```

### 3. Seção "Quality Check"

```
[Pipeline] { (Quality Check)
...
```

---

## 🔍 Como Encontrar o Erro

1. No Console Output, use **Ctrl+F** (buscar)
2. Procure por palavras-chave:
   - `ERROR:`
   - `FAILED`
   - `Exception`
   - `Error:`
   - `pytest`

3. **Copie a parte que mostra o erro** (últimas 100-200 linhas antes do "Deploy skipped")

---

## 🎯 Possíveis Problemas

### Se o erro for no Test:

Pode ser:
- Pytest não encontrado
- Módulo app não encontrado
- Erro de importação
- Todos os testes falhando

### Se o erro for no Build:

Pode ser:
- Python não encontrado
- Dependências não instaladas
- Ambiente virtual não criado

---

**Me envie a parte do log que mostra o erro real!** 🔍

