import streamlit as st




st.title('OpenAI GPT-3 Streamlit Demo')
st.subheader('Demo chatbot')

userInput = st.text_area("Enter Some Text:", height=100)

# storing past history of chat.
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []



if st.button("Submit"):
    response = ("You are searching for :",userInput)

    st.session_state.past.append(userInput)
    st.session_state.generated.append(response)

    st.write(response)


