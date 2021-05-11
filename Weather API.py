# A simple program to demonstrate the usage of API to retrieve weather info of a city.

import requests
from pprint import pprint

API = 'c869f8ab76747d57c306703532eec102' # Login to https://openweathermap.org/api for your API key

city = input('Enter the name of the city:\t')
baseURL = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API + '&q=' + city
weatherData = requests.get(baseURL).json()

pprint(weatherData)