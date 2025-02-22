import streamlit as st

from styling import style
style()

# Heading
st.title("Ctrl Shift Intelligence")
st.markdown("\n"*5)

# Buttons for navigation
col1, col2, col3 = st.columns(3)


with col1:
    st.subheader("Education")
    if st.button("Topic Explainer"):
        st.switch_page("pages/Topic_Explainer.py")
    if st.button("Question Maker"):
        st.switch_page("pages/Question_Maker.py")
with col2:
    st.subheader("Content Creation")
    if st.button("ShakeSpear Says"):
        st.switch_page("pages/ShakeSpear_Says.py")

with col3:
    st.subheader("Business")
    if st.button("Customer Support"):
        st.switch_page("pages/Customer_Support.py")