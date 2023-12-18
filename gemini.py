import google.generativeai as gemini
import os
from dotenv import load_dotenv
load_dotenv()
def model():
    gemini.configure(api_key=os.getenv('API_KEY'))
    return gemini.GenerativeModel('gemini-pro')