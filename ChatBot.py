import streamlit as st
from streamlit_chat import message
import openai

#openai.api_key = OPENAI_KEY


# funciton that generate response 
def getresponse(prompt):
    
    
    message = prompt 
    
    return message



# title and subtitle of the app
st.title('OpenAI GPT-3 Streamlit Demo')
st.subheader('Demo chatbot')

# storing past history of chat.
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


# App starts from here 
userInput = st.text_area("Enter Some Text:", height=100)

if st.button("Submit"):
    userInput = st.text_area("Enter Some Text:", height=100)
    st.text_area("", height=150)

    st.session_state.past.append(userInput)
    st.session_state.generated.append(response)

    #st.write(OPENAI_KEY)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')