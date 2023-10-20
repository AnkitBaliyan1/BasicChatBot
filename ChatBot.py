import streamlit as st
from streamlit_chat import message
import openai

openai.api_key = "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"


# funciton that generate response 
def getresponse(prompt):
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature = 0.5,
        stop=None,
        max_token=30,
        n=1
    )
    
    message = response.choices[0].text 
    
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
    response = getresponse(userInput)

    st.session_state.past.append(userInput)
    st.session_state.generated.append(response)

    #st.write(response)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')