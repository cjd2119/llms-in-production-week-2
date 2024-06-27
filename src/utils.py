import os

import streamlit as st

def give_defensive_warning() -> None:
    """
    Let the user know that you can get incorrect answers.
    """
    st.warning("""We cannot guarantee the SQL generated will give you the answer you are looking for, especially as written.
               Be as precise as possible, and if you can, specify the tables in your database, and their schema.
               """, icon=None)

def get_openai_api_key() -> None:
    """
    Get the OpenAI API key from the user.
    """
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    os.environ["OPENAI_API_KEY"] = openai_api_key
    if not openai_api_key.startswith("sk-"):
        st.error("Please enter your OpenAI API key!", icon="⚠️")