import streamlit as st

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

# Heading
st.title("Heading")

# Buttons for navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Page 1"):
        st.switch_page("pages/page1.py")
with col2:
    if st.button("Page 2"):
        st.write("Page 2 is under construction.")
with col3:
    if st.button("Page 3"):
        st.write("Page 3 is under construction.")