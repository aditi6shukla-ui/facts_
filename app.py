import streamlit as st
import wikipedia

st.title("Universal Facts App")

word = st.text_input("Type any planet, animal, fruit, car brand, or country")

key = word.strip()

if key:
    try:
        summary = wikipedia.summary(key, sentences=2, auto_suggest=False)
        st.write(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        st.write(wikipedia.summary(e.options[0], sentences=2))
    except wikipedia.exceptions.PageError:
        pass


