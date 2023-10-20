import streamlit as st
from streamlit_chat import message
import openai

#openai.api_key = OPENAI_KEY
openai.api_key = st.secrets['OPENAI_KEY']


# funciton that generate response 
def getresponse(prompt):
    
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=100,
    stop=None,
    n=2
)


    message = response.choices[0].text

    #message = prompt 
    
    return message


# title and subtitle of the app

# storing past history of chat.
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []




def main():

    st.title('OpenAI GPT-3 Streamlit Demo')
    st.subheader('Demo chatbot')

    # App starts from here 
    userInput = st.text_area("Enter Some Text:", height=100)

    if st.button("Submit"):
        response = getresponse(userInput)

        st.session_state.past.append(userInput)
        st.session_state.generated.append(response)

        #st.write(OPENAI_KEY)

    if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

    
if __name__=='__main__':
    main()