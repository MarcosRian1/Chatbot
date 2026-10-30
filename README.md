<h1 align="center">Chatbot de Futebol</h1>

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um chatbot com Inteligência Artificial, voltado a responder perguntas e fornecer informações relacionadas ao futebol.

A aplicação utiliza o modelo **Gemini 3.5 Flash-Lite**, com interface interativa desenvolvida em Streamlit.

## 🚀 Funcionalidades

- Respostas geradas por Inteligência Artificial.
- Recuperação do histórico da conversa para manutenção do contexto.
- Interface interativa de chat.
- Tratamento de erros durante a geração de respostas.
- Configuração dos parâmetros de geração do modelo.

## ⚙️ Configurações do modelo

- **Modelo:** Gemini 3.5 Flash-Lite
- **Temperatura:** 0.4
- **Limite de saída:** 1.000 tokens
- **Contexto:** histórico de mensagens da conversa

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Gemini API:** geração de respostas com Inteligência Artificial.
- **Streamlit:** desenvolvimento da interface web.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

## 💻 Como executar localmente

Clone o repositório:

```bash
git clone https://github.com/MarcosRian1/Chatbot.git
```

Acesse a pasta do projeto:

```bash
cd Chatbot
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a chave da API do Gemini nas variáveis de ambiente, utilizando o nome de variável esperado pelo código.

Execute a aplicação:

```bash
python -m streamlit run app.py
```

## 🌐 Acesse a aplicação

O chatbot está disponível para acesso pelo link:

[**Assistente de Futebol — Streamlit**](https://assistentfut.streamlit.app/)
