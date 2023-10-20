import streamlit as st




st.title('OpenAI GPT-3 Streamlit Demo')
st.subheader('Demo chatbot')

userInput = st.text_area("Enter Some Text:", height=100)

if st.button("Submit"):
    st.write("You are searching for :",userInput)