import streamlit as st

st.title("Word Facts App")

facts = {
    "python": "Python is a high-level programming language created by Guido van Rossum.",
    "streamlit": "Streamlit turns Python scripts into web apps with minimal code.",
    "github": "GitHub is a platform for hosting and collaborating on code using Git.",
    "india": "India is the world’s most populous country as of 2023."
}

word = st.text_input("Type a word")

word = word.lower().strip()

if word:
    if word in facts:
        st.write(facts[word])
    else:
        st.write("No fact found for this word.")
