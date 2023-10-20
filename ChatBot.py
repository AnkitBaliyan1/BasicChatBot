import streamlit as st
from streamlit_chat import message



st.title('OpenAI GPT-3 Streamlit Demo')
st.subheader('Demo chatbot')

userInput = st.text_area("Enter Some Text:", height=100)

# storing past history of chat.
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []



def getresponse(prompt):
    message = str("your output is : ",prompt)
    
    return message


if st.button("Submit"):
    response = getresponse(userInput)

    st.session_state.past.append(userInput)
    st.session_state.generated.append(response)

    #st.write(response)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')