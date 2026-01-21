import streamlit as st

st.title("Universal Facts App")

planets = {
    "mercury": "Mercury is the smallest planet and closest to the Sun.",
    "venus": "Venus is the hottest planet due to its thick atmosphere.",
    "earth": "Earth is the only known planet with life.",
    "mars": "Mars is called the Red Planet because of iron oxide.",
    "jupiter": "Jupiter is the largest planet in the solar system.",
    "saturn": "Saturn has the most visible ring system.",
    "uranus": "Uranus rotates on its side.",
    "neptune": "Neptune has the strongest winds in the solar system."
}

animals = {
    "dog": "Dogs were the first domesticated animals.",
    "cat": "Cats sleep up to 16 hours a day.",
    "elephant": "Elephants have the largest brains of any land animal.",
    "tiger": "Tigers have unique stripe patterns."
}

fruits = {
    "apple": "Apples float because they are 25% air.",
    "banana": "Bananas are berries botanically.",
    "mango": "Mangoes are the national fruit of India.",
    "orange": "Oranges are a hybrid fruit."
}

cars = {
    "tesla": "Tesla popularized mass-market electric cars.",
    "toyota": "Toyota is the world’s largest car manufacturer.",
    "bmw": "BMW originally made aircraft engines.",
    "ford": "Ford introduced the moving assembly line."
}

countries = {
    "india": "India has the largest democracy in the world.",
    "japan": "Japan has over 6,000 islands.",
    "france": "France is the most visited country in the world.",
    "brazil": "Brazil contains most of the Amazon rainforest."
}

facts = {**planets, **animals, **fruits, **cars, **countries}

word = st.text_input("Type any planet, animal, fruit, car brand, or country")

key = word.strip().lower()

if key in facts:
    st.write(facts[key])

