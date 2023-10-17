import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.prompt_pattern import PromptPattern
from genai.schemas import GenerateParams


##
# This is the E-waste Campaigning module provides the content for the E-waste campagining advertisement and SMS based campaigning for the general awareness on the E-waste.
# The module generates the text content based on the provided fact sheet on E-waste awareness and the prompt instruction.
# This module is using "ibm/granite-13b-instruct-v1" from IBM AI Lab and "google/flan-t5-xxl" for generating the text based on the provided prompt.  
##

load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_endpoint = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint)

#Providing data related to electronic waste recycling facilities
fact_sheet_ewaste = """
OVERVIEW
- Electronic waste recycling facilities, often called e-waste recycling centers, are specialized facilities designed to manage and process electronic waste.
- E-waste includes discarded electronic devices like smartphones, computers, laptops, TVs, printers, and more.
- These facilities play a crucial role in preventing environmental damage caused by improper disposal of electronic waste.
- Electronic waste contains hazardous materials like lead, mercury, and cadmium, which can harm the environment if not managed properly.
- E-waste recycling centers are equipped with specialized equipment to safely dismantle and process electronic devices.
- Valuable components like precious metals (gold, silver, copper) are separated for reuse in new electronics.
- E-waste recycling centers often collaborate with certified disposal facilities to manage hazardous waste properly.
- Some recycling facilities focus on refurbishing and reselling still-functioning electronics.
- Recycling helps conserve natural resources by reducing the need for mining and manufacturing raw materials.
- Proper disposal of e-waste prevents the release of toxic substances into the environment.
- Many countries have regulations and standards for the operation of e-waste recycling facilities to ensure environmental safety.
- Electronic waste recycling contributes to job creation and economic growth in the recycling industry.
- Recycling centers may offer drop-off locations for individuals and businesses to dispose of e-waste.
- Some facilities provide pick-up services for larger quantities of electronic waste.
- Public awareness campaigns often encourage responsible e-waste disposal and recycling.
- E-waste recycling facilities contribute to reducing landfill waste, which can take years to decompose.
- Recycled materials from e-waste can be used in various industries, including electronics, construction, and automotive.
- Recycling centers may employ eco-friendly practices, such as energy-efficient equipment and waste reduction techniques.
- Electronic waste recycling helps mitigate the carbon footprint associated with manufacturing new electronics.
- The growth of the electronics industry has led to an increase in e-waste, making recycling facilities even more essential.
- Many e-waste recycling facilities operate under the principles of the circular economy, promoting resource efficiency and sustainability.
- Some recycling centers engage in research and development to find innovative ways to recycle electronics more efficiently.
- E-waste recycling facilities must adhere to safety and environmental regulations to protect workers and the surrounding community.
- Recycling centers often partner with electronics manufacturers to recover and recycle their products responsibly.
- Environmental audits and certifications may be obtained by recycling facilities to demonstrate their commitment to sustainability.
- Some e-waste recycling centers offer data destruction services to ensure the security of sensitive information on devices.
- The global e-waste problem has led to international efforts to standardize e-waste recycling practices.
- Electronic waste recycling facilities contribute to reducing greenhouse gas emissions by reducing the need for new manufacturing.
- Some recycling centers offer educational programs to inform the public about the importance of recycling electronic waste.
- Recycling facilities may provide certificates of recycling to individuals and businesses as proof of responsible disposal.
- E-waste recycling centers support the development of a closed-loop system for electronics.
- Proper e-waste recycling reduces the energy consumption associated with mining and refining raw materials.
- Recycling electronic waste conserves water resources, as mining and manufacturing processes are often water-intensive.
- Some e-waste recycling centers offer incentives or discounts for recycling old electronics.
- Recycling facilities often work closely with local municipalities to ensure proper waste management.
- Electronic waste recycling helps reduce the demand for landfill space, which is often limited in urban areas.
- The recycling process includes testing and refurbishing electronics whenever possible.
- Some recycling centers accept electronic accessories like chargers and cables for recycling.
- E-waste recycling facilities can recover valuable materials from old, obsolete electronics.
- Some recycled materials, like copper, can be of higher purity than newly mined resources.
- Responsible e-waste recycling helps reduce the environmental impact of the electronics industry.
- Recycling facilities may participate in e-waste collection events to encourage community involvement.
- Many electronic manufacturers now design products with recyclability in mind to facilitate the recycling process.
- Electronic waste recycling facilities are vital for creating a sustainable future by reducing the environmental impact of electronics consumption.


RECYCLING ELECTRONICS
- Smartphone
- Laptop
- Computer
- Tablet
- Smartwatch
- Digital camera
- Television
- Blu-ray player
- Home theater system
- Wireless router
- Gaming console
- E-book reader
- GPS navigation system
- MP3 player
- Wireless earbuds
- Wired headphones
- Speaker
- Digital voice recorder
- Fitness tracker
- Portable power bank
- Electric toothbrush
- Microwave oven
- Refrigerator
- Washing machine
- Dishwasher
- Air conditioner
- Vacuum cleaner
- Coffee maker
- Blender
- Food processor
- Electric kettle
- Rice cooker
- Toaster
- Hair dryer
- Curling iron
- Flat iron (hair straightener)
- Electric shaver
- Electric fan
- Space heater
- Cordless phone
- Cordless landline phone
- Alarm clock
- Smoke detector
- Wi-Fi extender
- Car alarm system
- Home security camera
- Drone
- Action camera
- Virtual reality headset (VR)
- 3D printer
- Handheld game console (e.g., Nintendo Switch)
- Digital scale
- Smart thermostat
- Portable DVD player
- DVD recorder
- Digital photo frame
- LED light bulbs

"""

def advertisement_prompt_template():
    #Returning prompt template for advertisement generation
    return (
        'Generate a advertisement in maximum 10 bullet points of our Electronic Waste Recycling Facily which will be displayed publically for following content.'
        "Content:\n\n"
        f"{fact_sheet_ewaste}\n\n"
    )

def create_advertisement():
    #Adding parameters and model granite-13b-instruct-v1 for advertisement generation
    params = GenerateParams(
    decoding_method="greedy",
    max_new_tokens=200,
    min_new_tokens=50,
    temperature=0.1
    )
    model = Model("ibm/granite-13b-instruct-v1", params=params, credentials=creds)
    pt = PromptPattern.from_str(advertisement_prompt_template())
    #Fetching the response for our prompt template
    responses = model.generate([pt])
    for response in responses:
        generated_ad=response.generated_text
    return(generated_ad)

def sms_prompt_template():
    #Fetching the generated advertisement as our reference
    ref_ad='\n'.join(create_advertisement().strip().split('\n')[1:-1])
    #Returning prompt template for SMS generation
    return (
        'Generate a mobile SMS for our Electronic Waste Recycling Facily which will be displayed publically for following content.'
        "Content:\n\n"
        f"{ref_ad}\n\n"
    )

def create_sms():
    #Adding parameters and model google/flan-t5-xxl for SMS generation
    params = GenerateParams(
    decoding_method="greedy",
    max_new_tokens=70,
    min_new_tokens=30,
    temperature=0.7
    )
    model = Model("google/flan-t5-xxl", params=params, credentials=creds)
    pt = PromptPattern.from_str(sms_prompt_template())
    #Fetching the response for our prompt template
    responses = model.generate([pt])
    for response in responses:
        generated_sms=response.generated_text
    return(generated_sms)
