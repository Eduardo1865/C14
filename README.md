# 🚀 C14
Repo para a aula de C14

---
## Para o projeto que está no Atividade1

## 🎯 QUIZ - Jogo de Perguntas e Respostas

Este projeto é um **jogo de quiz interativo** desenvolvido em Python usando a biblioteca PyQt5 para interface gráfica. O jogo apresenta as seguintes funcionalidades:

### 📋 Funcionalidades Principais:

- **Interface Gráfica Intuitiva**: Menu principal com opções para iniciar o quiz e configurar opções
- **Perguntas Online**: Utiliza a API do Open Trivia Database (opentdb.com) para buscar perguntas em tempo real
- **Níveis de Dificuldade**: Permite escolher entre três níveis de dificuldade:
  - Fácil
  - Médio  
  - Difícil
- **Configuração Personalizável**: 
  - Número de perguntas (1 a 20)
  - Seleção de dificuldade
- **Sistema de Pontuação**: Acompanha os acertos em tempo real
- **Perguntas de Múltipla Escolha**: Cada pergunta possui 4 alternativas
- **Resultado Final**: Exibe a pontuação total ao final do quiz

### 🏗️ Estrutura do Projeto:

- `menu.py` - Tela principal do jogo com menu de navegação
- `jogo.py` - Lógica principal do quiz e interface do jogo
- `opcoes.py` - Janela de configurações para personalizar o quiz
- `menu.spec` - Arquivo de configuração para build do executável

## Como rodar?
Tem um arquivo executavel, é só clicar nele

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

### 5. Executar o projeto - forma alternativa
Para executar o menu principal do quiz:

```powershell
pipenv run python menu.py
```

Ou simplesmente clicar no executável.
