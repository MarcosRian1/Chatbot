import streamlit as st
from google import genai
from google.genai import types
from functions import get_secret

# Pegando dados da API conectada
api_key = get_secret('API_KEY')

# Instanciando o SDK
client = genai.Client(api_key=api_key)

# Se não houver nenhum contexto na conversa, inicializa como vazio
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Instruções para o prompt
if not st.session_state.chat_history:
    st.session_state.chat_history.append(('assistant', 
                                          '''
                                          Olá, eu sou um assistente de futebol. 
                                          
                                          Você pode me perguntar sobre curiosidades como impedimento, novas regras ou toque
                                          de mão.

                                          Posso responder sobre jogadores de futebol que atuam ou que se aposentaram.

                                          Também posso responder sobre eventos passados como campeonatos locais ou Copa
                                          do Mundo.

                                          Como posso te ajudar?
                                          '''))

# Entrada do usuário
user_message = st.chat_input('Escreva sua mensagem...')

# Retorna na tela toda a interação
for role, message in st.session_state.chat_history:
    st.chat_message(role).write(message)

if user_message:
    # Retorna o que o usuário escreveu no momento
    st.chat_message('user').write(user_message)
    # Adiciona a mensagem ao histórico
    st.session_state.chat_history.append(('user', user_message))

    with st.spinner('O agente está pensando'):

        # Restrições e orientações do que o chatbot deve responder
        system_prompt = f"""
        Você é um assistente de futebol.
        Sempre explique conceitos de forma didática mas também curta usando uma linguagem clara e simples. Use também exemplos
        quando necessário.
        Se o usuário perguntar coisas não relacionadas a futebol responda de forma gentil que não é possível responder sobre 
        isso, não responda também sobre derivados do futebol.
        """

        # Pegando o system_prompt para retornar o contexto com a mensagem do usuário
        full_input = f"{system_prompt}\n\nMensagem do usuário:\n\"\"\"{user_message}\n\"\"\""

        # Resgatando todo o contexto da conversa
        context = [
            *[
                {'role': role, 'parts': [{'text': msg}]} for role, msg in st.session_state.chat_history
            ],
            # Retorna a ultima mensagem
            {'role': 'user', 'parts': [{'text': full_input}]}
        ]

        # Configurações da resposta como modelo, contexto e segurança    
        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=context,
            config=types.GenerateContentConfig(
                safety_settings = [
                    types.SafetySetting(
                    category='HARM_CATEGORY_HATE_SPEECH',threshold='BLOCK_ONLY_HIGH'),
                ],
                max_output_tokens=1000,
                temperature=1
            )
        )

        # Retorno apenas do texto da resposta
        assistant_reply = response.text

        # Escreve na tela
        st.chat_message('assistant').write(assistant_reply)
        # Adiciona ao contexto da conversa
        st.session_state.chat_history.append(('assistant', assistant_reply))