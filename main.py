import logging
import requests
from twilio.twiml.messaging_response import MessagingResponse
import pycountry

def whatsapp_webhook(request):
    """HTTP Cloud Function.
    Parameters
    ----------- 
    request (flask.Request) : The request object
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
   
    Returns
    ----------
    The response text, or any set of values that can be turned into a
    Response object using `make_response`
    <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    country = request.values.get('Body', "").lower()
    alpha_3 = pycountry.countries.search_fuzzy(country)[0].alpha_3

    resp = requests.get(f'https://vaccovid.live/api/api-covid-data/provinces-report-iso-based/{alpha_3}')

    twilio_resp = MessagingResponse()

    msg = twilio_resp.message()

    if not (200 <= resp.status_code <= 299):
        logger.error({'message':f'Could not retrive information for given country: {country}','Reason': resp.reason })
        msg.body(f'Sorry request for country: {country} could not be processed, please try again or ensure country name is spelt correctly')

    else:
        data = resp.json()[0]
        confirmed = data['confirmed']
        recovered = data['recovered']
        deaths = data['deaths']
        case_fatality_rate = data['Case_Fatality_Rate']
        active = data['active']
        msg.body(f'''
        Updates for covid cases in {country}:
        Confirmed Cases: {confirmed}
        Recovered Cases: {recovered}
        Deaths         : {deaths}
        Active	       : {active}
        Case Fatal Rate: {case_fatality_rate}
        ''')

    return str(twilio_resp)


