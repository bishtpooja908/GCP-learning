import streamlit as st
from db_config import insert_user, get_all_users

st.title("🚀 My First Streamlit App with MySQL")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"You are {age} years old.")

if st.button("Greet Me"):
    if name.strip():
        if insert_user(name, age):  
            st.success(f"Hello, {name}! Welcome to Streamlit 🎉")
        else:
            st.error("❌ Failed to save user.")
    else:
        st.warning("⚠️ Name cannot be empty.")
