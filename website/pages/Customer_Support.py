import streamlit as st
from classes import initial_customer_support_response, get_response  # Replace with your actual function
from styling import style

style()


# Initialize session state for chat history
if "chat_history" not in st.session_state:

    from prompts import base, customer_support_prompt
    st.session_state.chat_history = [
        {"role":"developer", "content":base+customer_support_prompt},
        {"role":"assistant", "content":"Ok. I will follow as instructed"},
    ]


print("\n\n\n\n", st.session_state.chat_history, "\n chathistory up\n")


# Page title
st.title("Customer Support")

# Display chat history at the top
if len(st.session_state.chat_history)!=2:
    st.subheader("Chat History")
    
for message in st.session_state.chat_history[2:]:
    if message['role']=='developer': continue
    st.write(f"**{f':blue[Support Agent]' if message['role']=='assistant' else f':green[User]'}**: {message['content']}")

# Input fields for subject and topic (only show if chat history is empty)
print("len: ", len(st.session_state.chat_history))

if len(st.session_state.chat_history)==2:#    and ( "topic" not in st.session_state) and ("subject" not in st.session_state):
    
    with st.form(key='input_form'):
        
        st.write("Enter the Bill ID, along with either product name or product id")
        
        bill_id = st.text_input(label="Bill ID:", key='bill_id')
        product_name = st.text_input(label="Name of product:", key='product_name')
        product_id = st.text_input(label='Product ID: ', key='product_id')
        issue = st.text_area(label="Issue(s) being faced with the product", key='issue')

        # Button to submit inputs
        if st.form_submit_button("Submit"):
            if not bill_id:
                response = f"Enter Bill ID"
                st.write(response)
            elif not product_id and not product_name:
                response = "Enter either product name or product id"
                st.write(response)
            elif not issue:
                response = 'Please describe your issue'
                st.write(response)
            else:
                response = initial_customer_support_response(issue=issue, messages=st.session_state.chat_history, bill_id=bill_id,  product_id=product_id, product_name=product_name)
                if (response==-1):
                    st.write("Enter proper bill ID")
                else:
                    st.session_state.chat_history.append({"role":"assistant",  'content':response})
                

            # Add user input and chatbot response to chat history
            # st.session_state.chat_history.append({"role":"user", "content":author})
            # st.session_state.chat_history.append({"role":"assistant", "content":response})

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
