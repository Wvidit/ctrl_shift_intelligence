import streamlit as st



# Import your custom function from your Python script
# Replace `your_script` with the actual name of your script
from classes import get_response  # Replace with your actual function


from styling import style
style()


# Initialize session state for chat history
if "chat_history" not in st.session_state:

    from prompts import base, content_creation_prompt
    st.session_state.chat_history = [
        {"role":"developer", "content":base+content_creation_prompt},
        {"role":"assistant", "content":"Ok. I will follow as instructed"},
    ]


print("\n\n\n\n", st.session_state.chat_history, "\n chathistory up\n")


# Page title
st.title("ShakesPear Says")

# Display chat history at the top
if len(st.session_state.chat_history)!=2:
    st.subheader("Chat History")
    
for message in st.session_state.chat_history[2:]:
    st.write(f"**{f':blue[Chatbot]' if message['role']=='assistant' else f':green[User]'}**: {message['content']}")

# Input fields for subject and topic (only show if chat history is empty)
print("len: ", len(st.session_state.chat_history))

if len(st.session_state.chat_history)==2:#    and ( "topic" not in st.session_state) and ("subject" not in st.session_state):
    
    with st.form(key='input_form'):
        author = st.text_area(label="ShakesPear here! What do you want me to act as?", key='author', value='Shakespeare')

        # Button to submit inputs
        if st.form_submit_button("Submit"):
            if author:
                # Call your function with 2 arguments
                response = f"Hey it's {author} here!"
            else:
                response = f"Hey it's ShakesPear here!"
                

            # Add user input and chatbot response to chat history
            st.session_state.chat_history.append({"role":"user", "content":author})
            st.session_state.chat_history.append({"role":"assistant", "content":response})

# Input for additional messages (always show at the bottom)
else:
    user_message = st.text_input("Enter your message:", key="user_input", value=None)

    if st.button("Send"):
        if user_message:
            # Call your function with the user's message
            response = get_response(user_message, messages=st.session_state.chat_history)

            # Add user input and chatbot response to chat history
            st.session_state.chat_history.append({"role":"assistant", "content":response})

            # Clear the input box after sending the message
            # st.session_state.user_input = ""  # Reset the session state for the input box
        else:
            st.write("Please enter a message.")
