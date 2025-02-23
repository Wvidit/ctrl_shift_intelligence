import streamlit as st

def style():
    
    st.set_page_config(layout="wide")

    # if 'counter' not in st.session_state:
    #     st.session_state.counter = 1
    
    # if (st.session_state.counter%2):
    #     st.rerun()
    #     st.session_state+=1
    

    # Custom CSS for styling
    st.markdown(
        """
        <style>
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
