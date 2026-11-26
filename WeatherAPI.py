import requests
"""
Can only return these value 
-TEMPERATURE
-FEELSLIKE
-HUMIDITY
-PRECIPITATION
-WIND
-UV
-WEATHER
"""

def TodayWeather(city, task): # need to make parameters the name of the city and what 
                    #the user is asking for 
    BASE_URL_Front = "https://wttr.in/"
    BASE_URL_End = "?format=j1"
    fullUrl = BASE_URL_Front + city + BASE_URL_End


    #needInfo = some tuple that voice helpers will return that will use the api
                # to get the values

    try:
        info = requests.get(fullUrl).json()
        if task == "WEATHER":
            tempF = info["current_condition"][0]["temp_F"]
            weatherD = info["current_condition"][0]["weatherDesc"][0]["value"]

            return(f"The temperture in {city} is {tempF} and the weather is {weatherD}.")
        
        elif task == "TEMPERATURE":
            tempF = info["current_condition"][0]["temp_F"]

            return f"The temperture in {city} is {tempF}"
        
        elif task == "FEELSLIKE":
            feelsL = info["current_condition"][0]["FeelsLikeF"]

            return f"The temperture in {city} feels like {feelsL}."

        elif task == "HUMIDITY":
            humid = info["current_condition"][0]["humidity"]

            return f"The humidity in {city} is {humid} percent."

        elif task == "PRECIPITATION":
            precip = info["current_condition"][0]["precipInches"]

            return f"The precipation in {city} is {precip} inches."

        elif task == "WIND":
            wind = info["current_condition"][0]["windspeedMiles"]

            return f"The wind speed in {city} is {wind} miles per hour."

        elif task == "UV":
            uv = info["current_condition"][0]["uvIndex"]

            return f"The UV in {city} is {uv}."
    except:
        print("Invalid City/Task")
        return


