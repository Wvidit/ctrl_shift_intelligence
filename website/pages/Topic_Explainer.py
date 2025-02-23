import streamlit as st
from classes import initial_topic_explainer_response, get_response  
from styling import style
style()


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}
    

# Initialize session state for chat history
if "topic_explainer" not in st.session_state.chat_history:

    from prompts import base, topic_explainer_prompt
    st.session_state.chat_history['topic_explainer'] = [
        {"role":"developer", "content":base+topic_explainer_prompt},
        {"role":"assistant", "content":"Ok. I will follow as instructed"},
    ]


print("\n\n\n\n", st.session_state.chat_history['topic_explainer'], "\n chathistory up\n")


# Page title
st.title("Topic Explainer")

# Display chat history at the top
if len(st.session_state.chat_history['topic_explainer'])!=2:
    st.subheader("Chat History")
    
for message in st.session_state.chat_history['topic_explainer'][2:]:
    st.write(f"**{':blue[Chatbot]' if message['role']=='assistant' else ':green[User]'}**: {message['content']}")

# Input fields for subject and topic (only show if chat history is empty)
print("len: ", len(st.session_state.chat_history['topic_explainer']))

if len(st.session_state.chat_history['topic_explainer'])==2:#    and ( "topic" not in st.session_state) and ("subject" not in st.session_state):
    
    with st.form(key='input_form'):
        subject = st.text_input("Enter Subject:", key="subject")
        topic = st.text_input("Enter Topic:", key="topic")

        # Button to submit inputs
        if st.form_submit_button("Submit"):
            if subject and topic:
                # Call your function with 2 arguments
                response = initial_topic_explainer_response(subject=subject, topic=topic, messages=st.session_state.chat_history['topic_explainer'])
            else:
                response = "Please provide at least one input."

            st.session_state.chat_history['topic_explainer'].append({"role":"assistant", "content":response})

# Input for additional messages (always show at the bottom)
else:
    user_message = st.text_input("Enter your message:", key="user_input", value=None)

    if st.button("Send"):
        if user_message:
            # Call your function with the user's message
            response = get_response(user_message, messages=st.session_state.chat_history['topic_explainer'])

            # Add user input and chatbot response to chat history
            st.session_state.chat_history['topic_explainer'].append({"role":"assistant", "content":response})
        
        else:
            st.write("Please enter a message.")
