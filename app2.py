import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
env_var = os.getenv("GEMINI_APP_KEY")
print(env_var)