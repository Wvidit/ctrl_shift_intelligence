import streamlit as st

# Import your custom function from your Python script
# Replace `your_script` with the actual name of your script
from classes import TopicExplainer  # Replace with your actual function

topic_assistant = TopicExplainer()

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput input {
        color: black;
        background-color: white;
    }
    .stButton button {
        background-color: lightblue;
        color: black;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton button:hover {
        background-color: #add8e6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set page background color
st.markdown(
    """
    <style>
    body {
        background-color: darkblue;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page title
st.title("Chatbot Page")

# Input fields for subject and topic
subject = st.text_input("Enter Subject:")
topic = st.text_input("Enter Topic:")

# Button to submit inputs
if st.button("Submit"):
    if subject and topic:
        # Call your function with 2 arguments
        response = topic_assistant.get_response(subject, topic)
    else:
        response = "Please provide at least one input."

    # Add user input and chatbot response to chat history
    st.session_state.chat_history.append(("You", f"Subject: {subject}, Topic: {topic}"))
    st.session_state.chat_history.append(("Chatbot", response))

# Display chat history
st.subheader("Chat History")
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")

# Input for additional messages
user_message = st.text_input("Enter your message:")
if st.button("Send"):
    if user_message:
        # Call your function with the user's message
        response = topic_assistant.get_response(user_message)
        # Add user input and chatbot response to chat history
        st.session_state.chat_history.append(("You", user_message))
        st.session_state.chat_history.append(("Chatbot", response))
        # Clear the input box after sending the message
        user_message = ""  # This ensures the input box is cleared
    else:
        st.write("Please enter a message.")

# Display chat history
st.subheader("Chat History")
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")