import os
import pathlib

from dotenv import load_dotenv

from genai.credentials import Credentials
from genai.model import Model
from genai.prompt_pattern import PromptPattern
from genai.schemas import GenerateParams

##
# This is the E-waste seggregation module. The module function seggregation_model() seggregates the electronic devices to the respective E-waste category based on the model training data.
# This module is using "ibm/granite-13b-instruct-v1" model from the IBM research lab for the E-waste seggregation. 
##

# The GENAI_KEY and GENAI_API keys will be loaded from the .env file added to the project root for SDK API calls
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_endpoint = os.getenv("GENAI_API", None)
PATH = pathlib.Path(__file__).parent.resolve()
   

# Seggregation function that accepts array of devices and returns the generated_text output recieved from model 
def seggregation_model(test_devices: list[str]):

    # Model parameters to be specified for model configuration
    params = GenerateParams(
        decoding_method="greedy",
        repetition_penalty=1,
        max_new_tokens=512,
        min_new_tokens=10,
        stream=False,
        temperature=0.7
        )
    
    # Credentials object with the above GENAPI_KEYS
    creds = Credentials(api_key, api_endpoint)
    model = Model("ibm/granite-13b-instruct-v1", params=params, credentials=creds)

    # Python dict to collect the model output for each device
    generated_output = {}

    pt = PromptPattern.from_file(str(PATH) + os.sep + "assets" + os.sep + "e-waste.yaml")

    for device in test_devices: 
        pt.reset()
        pt.sub("obj", device)
        gen_responses = model.generate_as_completed([str(pt)])
        response = gen_responses.__next__()
        generated_output[device] = response.generated_text

    return generated_output
