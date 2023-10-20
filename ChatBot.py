import streamlit as st
import openai
from streamlit_chat import message


openai.api_key = OPENAI_KEY

def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.5,
        max_tokens=100,
        stop=None,
        n=1
    )
    message = response.choices[0].text
    return message




st.title('OpenAI GPT-3 Streamlit Demo')
st.subheader('Demo chatbot')
