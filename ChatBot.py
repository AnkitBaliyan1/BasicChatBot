import streamlit as st
import openai
from streamlit_chat import message


openai.api_key = OPNEAI_KEY

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

#user_input = st.text_area("Enter some text:", height=150)


# storing past history of chat.
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


user_input=st.text_area("Enter some text: (Max word out:100)", height=150)
if st.button("Submit"):
    output = generate_response(user_input)
    # store output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')