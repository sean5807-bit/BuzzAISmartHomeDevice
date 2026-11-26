from WeatherAPI import TodayWeather

def main():

    response = input("What would you like to ask? ")

    if "weather" in response.lower():
        iWeather = response.index("weather")
        iCity = iWeather + 11
        city = response[iCity:]
        task = "WEATHER"
        print(TodayWeather(city, task))

    else:
        print("Invalid Response")
while True:
    main()