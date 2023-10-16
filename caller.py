#!/usr/bin/env python
# encoding: utf-8

from decimal import Decimal
from flask import Flask,jsonify
from modules.ewaste_analysis import getMobileStats
from modules.ewaste_campaign import create_advertisement
from modules.ewaste_campaign import create_sms
import html

# Instantiating the flask app object for the caller module 
app = Flask(__name__)
app.json.sort_keys = False


# App route for the e-waste analysis API call 
@app.route('/smartphone_analysis')
def getPhoneEWasteAnalysis():

    # Get function call to obtain the data from the AI model on e-waste generation 
    ewaste_in_india_in_million_tons , percent_phone_ewaste_in_state = getMobileStats()

    # Converting the string data into the int format for the calculation
    mobile_ewaste_percent_num = int(percent_phone_ewaste_in_state.replace('%',''))
    ewaste_num = Decimal(ewaste_in_india_in_million_tons.split(' ')[0])
    mobile_ewaste = (ewaste_num * mobile_ewaste_percent_num) / 100
    
    # Calculating the expected e-waste to be recycled per state and generating the analysis for the final response 
    no_of_states_in_india = 28
    avg_mobile_ewaste_expected = round((mobile_ewaste/no_of_states_in_india) * 1000000,2)
    analysis = "Average Mobile EWaste is expected at state level is "+str(avg_mobile_ewaste_expected) + " Tons, but actual value is X Tons"
    analysis = analysis + " The shortage suggests a  better campaiging strategy for mobile EWaste collection at state level"


    # The final output in the Python Dict to be returned as JSON response
    data = { 
            "AI Model value for Total EWaste per year in India" : ewaste_in_india_in_million_tons , 
            "AI Model value for Percent Mobile contribution to EWaste" : percent_phone_ewaste_in_state,
            "Total Mobile EWaste per year" : str(mobile_ewaste) + " Million Tons",
            "No of States in India" : 28,
            "Avg Mobile EWaste expected from a state per year" : str(avg_mobile_ewaste_expected) + " Tons",
            "Say Mobile EWaste collected at seggregation facility for a state": "X Million Tons",
            "Analysis" : analysis,
        } 
    
    return jsonify(data) 


# App route for the e-waste seggregator API call
@app.route('/seggregation')
def getPhoneEWasteAnalysis(devices):
    #data =  sushant's model

    data = {
        "computer":"got stored in rack ..........",
        "phone":"",
        "medical devices":""
    }

    return jsonify(data) 


# App route for the e-waste advertising API call
@app.route('/adv')
def getAdvertisement():
    #Removing the first and last line of the advertisement and adding our contact at the end
    ad = '\n'.join(create_advertisement().strip().split('\n')[1:-1])+"\nFor more information visit XYZ\n"
    return(html.escape(ad))

# App route for the SMS based advertising API call
@app.route('/sms')
def getSMS():
    #Removing last two lines of the SMS, providing health warning at the begining and adding our contact at the end
    sms = "E-waste is hazardous to human health. "+ (('. '.join(create_sms().split('. ')[:-2])).replace('. - ', '. ')).replace('Electronic Waste','E-waste') +".\nFor more information visit XYZ\n"
    return(sms)


# Main module condition for the flask app module
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
