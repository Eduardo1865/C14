# 🚀 C14
Repo para a aula de C14

---
## Para o projeto que está no Atividade1

## 📦 Instalação do Pipenv

### 1. Instalar o Pipenv
Abra o terminal (PowerShell no Windows) e execute:

```powershell
pip install pipenv
```

### 2. Verificar instalação
Execute:

```powershell
pipenv --version
```

### 3. Instalar dependências do projeto
Para instalar as dependências listadas no `Pipfile`:

```powershell
cd Atividade1
pipenv install
```

### 4. Ativar ambiente virtual
Para ativar o ambiente virtual do Pipenv:

```powershell
pipenv shell
```

### 5. Executar o projeto
Para executar o menu principal do quiz:

```powershell
pipenv run python menu.py
```

---
## Para o projeto que está no C14_juju2

## 📦 Instalação do Poetry

### 1. Instalar o Poetry
Abra o terminal (PowerShell no Windows) e execute:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2. Verificar instalação
Feche e abra o terminal novamente, depois execute:

```powershell
poetry --version
```

### 3. Instalar dependências do projeto
Para instalar as dependências listadas no `pyproject.toml`:

```powershell
poetry install
```

### 4. Ativar ambiente virtual
Para ativar o ambiente virtual do Poetry:

```powershell
poetry shell
```

---

## 🔧 Como Corrigimos o Conflito do Merge

### 📋 Comandos Utilizados:

**1. Verificar situação do repositório:**
```bash
git status
```

**2. Buscar mudanças no repositório remoto:**
```bash
git fetch origin
```

**3. Baixar e integrar as mudanças:**
```bash
git pull origin main
```

> ✅ **Resultado:** Conflito resolvido com sucesso!

---

