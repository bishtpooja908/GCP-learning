import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Input text
name = st.text_input("Enter your name:")

# Button + Output
if st.button("Greet Me"):
    st.success(f"Hello, {name}! Welcome to Streamlit 🎉")

# Slider
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"You are {age} years old.")

