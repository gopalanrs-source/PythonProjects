import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

city = input("Enter the city name: ")



def get_weather(city):
    print("Getting weather data for", city)

    request_url = f'https://api.openweathermap.org/data/3.0/onecall?&q={city}&appid={os.getenv("API_KEY")}&units=metric'

    print("Request URL:", request_url)

    weather_data = requests.get(request_url).json()
    pprint(weather_data)



get_weather(city)