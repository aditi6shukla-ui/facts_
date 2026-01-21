import streamlit as st
import wikipedia

st.title("Universal Facts App")

word = st.text_input("Type any planet, animal, fruit, car brand, or country")

if word:
    try:
        result = wikipedia.summary(word, sentences=2)
        st.write(result)
    except wikipedia.exceptions.DisambiguationError as e:
        st.write(wikipedia.summary(e.options[0], sentences=2))
    except wikipedia.exceptions.PageError:
        pass


