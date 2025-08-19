# 🎮 Quiz Game - C14

> Um jogo de quiz interativo com interface gráfica moderna

---

## 📖 Sobre o Projeto

Bem-vindo ao **Quiz Game**! 🎉 

Este é um jogo de perguntas e respostas desenvolvido em Python com PyQt5, que oferece uma experiência divertida e educativa. O jogo busca perguntas em tempo real da internet e permite que você teste seus conhecimentos em diferentes níveis de dificuldade.

---

## ✨ Funcionalidades

### 🎯 **Core Features**
| Funcionalidade | Descrição |
|---|---|
| 🖥️ **Interface Gráfica** | Menu intuitivo e design limpo |
| 🌐 **Perguntas Online** | Conexão com Open Trivia Database |
| 📊 **Sistema de Pontuação** | Acompanhe seus acertos em tempo real |
| 🎲 **Perguntas Aleatórias** | Cada partida é única! |

### ⚙️ **Configurações Personalizáveis**
- 🎚️ **3 Níveis de Dificuldade**: Fácil, Médio e Difícil
- 📝 **Quantidade de Perguntas**: Escolha de 1 a 20 perguntas
- 🔄 **Múltipla Escolha**: 4 alternativas por pergunta

---

## 🏗️ Arquitetura do Projeto

```
Atividade1/
├── 🏠 menu.py      # Interface principal e navegação
├── 🎮 jogo.py      # Engine do quiz e gameplay
├── ⚙️ opcoes.py    # Configurações e preferências
├── 📦 menu.spec   # Build configuration
└── 🔧 Pipfile     # Dependências do projeto
```

---

## 🚀 Como Executar

### 🎯 **Método Rápido**
```bash
# Clique no arquivo executável
./menu.exe  # (se disponível)
```

### �️ **Método Desenvolvimento**

#### 1️⃣ **Setup do Ambiente**
```powershell
# Instalar Pipenv
pip install pipenv

# Verificar instalação
pipenv --version
```

#### 2️⃣ **Preparar Projeto**
```powershell
# Navegar para o diretório
cd Atividade1

# Instalar dependências
pipenv install

# Ativar ambiente virtual
pipenv shell
```

#### 3️⃣ **Executar o Jogo**
```powershell
# Iniciar o quiz
pipenv run python menu.py
```

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Versão | Uso |
|---|---|---|
| ![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python) | 3.12 | Linguagem principal |
| ![PyQt5](https://img.shields.io/badge/PyQt5-Latest-green?logo=qt) | Latest | Interface gráfica |
| ![Requests](https://img.shields.io/badge/Requests-Latest-orange?logo=python) | Latest | HTTP requests |
| ![PyInstaller](https://img.shields.io/badge/PyInstaller-Latest-red?logo=python) | Latest | Build executável |

</div>

---

## 🎮 Como Jogar

1. **🏁 Inicie** o jogo executando `menu.py`
2. **⚙️ Configure** suas preferências (opcional)
   - Escolha o nível de dificuldade
   - Defina a quantidade de perguntas
3. **🎯 Clique** em "Iniciar Quiz"
4. **📝 Responda** as perguntas de múltipla escolha
5. **🏆 Veja** sua pontuação final!

---

<div align="center">

**🎉 Divirta-se testando seus conhecimentos! 🧠**

*Desenvolvido para a disciplina C14* 

</div>
