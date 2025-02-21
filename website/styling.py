import streamlit as st

def style():
    
    st.set_page_config(layout="wide")

    st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

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