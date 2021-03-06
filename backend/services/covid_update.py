import requests
import json

def covid_update_local():
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"code":"bd"}

    headers = {
        'x-rapidapi-key': "9f21abce8amsh093201626652b21p1fcd62jsna52876fbd88c",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    return json.loads(response.text)

def covid_update_global():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    headers = {
        'x-rapidapi-key': "9f21abce8amsh093201626652b21p1fcd62jsna52876fbd88c",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)
