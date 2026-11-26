import requests
import voice_helpers


def TodayWeather(): # need to make parameters the name of the city and what 
                    #the user is asking for 
    BASE_URL_Front = "https://wttr.in/"
    BASE_URL_End = "?format=j1"
    city = "Shanghai" # need to make this a value returned by vocie helpers 
    fullUrl = BASE_URL_Front + city + BASE_URL_End


    #needInfo = some tuple that voice helpers will return that will use the api
                # to get the values


    info = requests.get(fullUrl).json()
    tempF = info["current_condition"][0]["temp_F"]
    weatherD = info["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"The temperture in {city} is {tempF} and the weather is {weatherD}.")
    # will eventually need to return this value 

TodayWeather()

    