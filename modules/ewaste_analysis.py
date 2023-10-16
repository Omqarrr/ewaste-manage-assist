import os
from flask import Flask
from dotenv import load_dotenv
from genai.extensions.langchain import LangChainInterface
from genai.schemas import GenerateParams
from genai.credentials import Credentials

# Add the ".env" file to the project root with the GENAI_KEY and GENAI_API keys to load the keys in the module as below 
load_dotenv()
api_key = os.getenv("GENAI_KEY", None) 
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url)

# Model parameters to specify the decoding_method,  
params = GenerateParams(decoding_method="greedy")

# Create a model instance specifying the model, model parameters and loaded GENAI keys
langchain_model = LangChainInterface(model="google/flan-t5-xxl", params=params, credentials=creds)

# Prompt pattern for collecting the e-waste generating data from the intended electronic segment and overall e-waste generated
ewaste_in_india_in_million_tons = langchain_model("Answer this question: How many lakh tonnes tons of ewaste is generated every year India ?")
percent_phone_ewaste_in_state = langchain_model("Answer this question: How many percent of people discard their smartphone and buy a new one every year in Maharashtra state of India ?")

# Get function to return the e-waste generation data from the model
def getMobileStats():
    return ewaste_in_india_in_million_tons, percent_phone_ewaste_in_state
