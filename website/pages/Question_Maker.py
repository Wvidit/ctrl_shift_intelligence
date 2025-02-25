import streamlit as st
from classes import initial_question_maker_response, get_response  # Replace with your actual function
from styling import style


style()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}
  

# Initialize session state for chat history
if "question_maker" not in st.session_state.chat_history:

    from prompts import base, question_maker_prompt
    st.session_state.chat_history['question_maker'] = [
        {"role":"developer", "content":base+question_maker_prompt},
        {"role":"assistant", "content":"Ok. I will strictly follow as instructed"},
    ]




print("\n\n\n\n", st.session_state.chat_history['question_maker'], "\n chathistory up\n")


# Page title
st.title("Question Maker")

# Display chat history at the top
if len(st.session_state.chat_history['question_maker'])!=2:
    st.subheader("Chat History")
for message in st.session_state.chat_history['question_maker'][2:]:
    st.write(f"**{':blue[Chatbot]' if message['role']=='assistant' else ':green[User]'}**: {message['content']}")

# Input fields for subject and topic (only show if chat history is empty)
print("len: ", len(st.session_state.chat_history['question_maker']))

if len(st.session_state.chat_history['question_maker'])==2:#    and ( "topic" not in st.session_state) and ("subject" not in st.session_state):
    
    with st.form(key='input_form'):
        subject = st.text_input("Enter Subject:", key="subject")
        topic = st.text_input("Enter Topic:", key="topic")
        question_count = st.text_input("Number of Questions: ", key='question_count', value='3')
        difficulty=st.text_input("Difficulty: ", key='difficulty', value='Moderate')

        # Button to submit inputs
        if st.form_submit_button("Submit"):
            if subject and topic:
                response = initial_question_maker_response(
                    subject=subject, 
                    topic=topic, 
                    question_count=question_count,
                    difficulty=difficulty,                    
                    messages=st.session_state.chat_history['question_maker'])
            else:
                response = "Please provide at least one input."

            # Add user input and chatbot response to chat history
            st.session_state.chat_history['question_maker'].append({"role":"assistant", "content":response})


# Input for additional messages (always show at the bottom)
else:
    user_message = st.text_input("Enter your message:", key="user_input", value=None)

    if st.button("Send"):
        if user_message:
            # Call your function with the user's message
            response = get_response(user_message, messages=st.session_state.chat_history['question_maker'])

            # Add user input and chatbot response to chat history
            st.session_state.chat_history['question_maker'].append({"role":"assistant", "content":response})
        else:
            st.write("Please enter a message.")
