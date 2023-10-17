import os
from flask import Flask
from dotenv import load_dotenv
from genai.extensions.langchain import LangChainInterface
from genai.schemas import GenerateParams
from genai.credentials import Credentials

##
# This is the E-waste analysis module, performing the analysis on E-waste generating from smartphone devices.
# This module is using the LangChainInterface from genai and "google/flan-t5-xxl" model for data source.    
##

# The GENAI_KEY and GENAI_API keys will be loaded from the .env file added to the project root for SDK API calls 
load_dotenv()
api_key = os.getenv("GENAI_KEY", None) 
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url)

# Model parameters to be specified for model configuration
params = GenerateParams(decoding_method="greedy")

# Create a model instance specifying the model, model parameters and loaded GENAI keys
langchain_model = LangChainInterface(model="google/flan-t5-xxl", params=params, credentials=creds)

# Prompt pattern for collecting the e-waste generating data from the intended electronic segment and overall e-waste generated
ewaste_in_india_in_million_tons = langchain_model("Answer this question: How many lakh tonnes tons of ewaste is generated every year India ?")
percent_phone_ewaste_in_state = langchain_model("Answer this question: How many percent of people discard their smartphone and buy a new one every year in Maharashtra state of India ?")

# Get function to return the e-waste generation data from the model
def getMobileStats():
    return ewaste_in_india_in_million_tons, percent_phone_ewaste_in_state
