import streamlit as st
from langchain.llms import GooglePalm
from PIL import Image
# Import necessary libraries for the chosen LLM (replace with actual code)
# For example (replace with your preferred LLM):
# from bard import Bardeen  # Assuming Bard is the chosen LLM
api_key = 'AIzaSyCeRGyW3FmGSmnl5ZJdH6keqYzMaiZs01U'






llm = GooglePalm(google_api_key=api_key, temperature=0.7)


    

st.set_page_config(
   
    page_title="GooglePalm Assistant🧠",
    page_icon="🚀",
    layout="centered")

# Streamlit app layout and functionality
st.title("GooglePalm Assistant🧠 ")

# Input text area for user to enter code-related queries
query = st.text_area("I'm Here to assist you write your query here 🗨️ ")

# Button to generate code based on the query
if st.button("Generate Solution"):
    if query:
        # Generate code using the GooglePalm model
        generated_code = llm(query)
        st.code(generated_code)
    else:
        st.warning("Please enter a query before generating code.")
