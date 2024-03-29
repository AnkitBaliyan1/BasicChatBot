# importing basic libraries
import streamlit as st
import openai 


openai.api_key = st.secrets['OPENAI_KEY']


def create_message(system_input, user_input):

    """
    This function can custom draft the message to be used to generate response.
    """

    message = [{'role':'system',
                'content':system_input},
                {'role':'user',
                'content':user_input}]    
    return message


def generate_response(system, user, model='gpt-3.5-turbo',
                      temperature=1, max_tokens=50):

    """
    This function will generate the response using prompt imput by user.
    The default model is 'gpt-3.5-turbo'
    The message is required to be in role:content format, 
        for which create message function is used.
    The paramets are set to default with max token as 50 and 
    max temperature randomness.

    The response so generated, is returned.
    
    """
    messages = create_message(system_input=system, user_input= user)

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message["content"]

def define_parameters():
    """
    Define parameters is to get the user input for assistant type and question. 
    This is also used to define the context for system role.

    Return:
        well defined system and user prompt.

    """

    assistant_type = st.selectbox("Chose how you want your assistant to be like.",
                                  ["Mathematician", "Doctor", "Data Scientist","Poet","Shashi Throor","Consultant"])
    
    
    system = f"""Act like {assistant_type} expert and respond to the user input. 
        Limit expertise to {assistant_type} field and do not answer any other subject matter. Clearly say sorry but politely.
        If the {assistant_type} is 'Mathematician' than answer should be numerical. Do not explain untill asked.
        if the {assistant_type} is doctor, Do not make any recomendation for any kind of drug and only
         explain with technical term in the response. 
        If the {assistant_type} is a poet than ryme the output line and limit the respone to 2 line poem.

        In any case, do not violate the moderation policy.
        Also, make sure your response is complete within 2 lines.
    """

    user = st.text_input("How can I help ?")

    return system, user

def main():
    st.title("LLM Version 2.0")
    system, user = define_parameters()

    if st.button("Get Response"):
        output = generate_response(system, user)
        st.write(output)

if __name__=="__main__":
    main()