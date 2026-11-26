import requests
import voice_helpers
"""
Can only return these value 
-TEMPERATURE
-FEELSLIKE
-HUMIDITY
-PRECIPITATION
-WIND
-CONDITION
-UV
-CLOUDS
-ALL
"""

def TodayWeather(city, task): # need to make parameters the name of the city and what 
                    #the user is asking for 
    BASE_URL_Front = "https://wttr.in/"
    BASE_URL_End = "?format=j1"
    fullUrl = BASE_URL_Front + city + BASE_URL_End


    #needInfo = some tuple that voice helpers will return that will use the api
                # to get the values


    info = requests.get(fullUrl).json()
    if task == "ALL":
        tempF = info["current_condition"][0]["temp_F"]
        weatherD = info["current_condition"][0]["weatherDesc"][0]["value"]

        print(f"The temperture in {city} is {tempF} and the weather is {weatherD}.")


    