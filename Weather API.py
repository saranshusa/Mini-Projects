# A simple program to demonstrate the usage of API to retrieve weather info of a city.

import requests
from time import sleep

API = 'c869f8ab76747d57c306703532eec102' # Login to https://openweathermap.org/api for your API key

city = input('Enter the name of the city:\t')
baseURL = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API + '&q=' + city
weatherData = requests.get(baseURL).json()

degree = u"\N{DEGREE SIGN}"
weatherDescription = weatherData["weather"][0]['description']
weather = weatherData["weather"][0]['main']
temperature = weatherData['main']['temp'] - 273.15
feelsLike = weatherData['main']['feels_like'] - 273.15
humidity = weatherData['main']['humidity']
maxTemperature = weatherData['main']['temp_max'] - 273.15
minTemperature = weatherData['main']['temp_min'] - 273.15
city = weatherData['name']
country = weatherData['sys']['country']
wind = weatherData['wind']['speed']

print(f'\nCity:\t\t{city}\n\
Country:\t{country}\n\
Weather:\t{weather}\n\
Temperature:\t{temperature:.1f} {degree}C\n\
Max:\t\t{maxTemperature:.1f} {degree}C\n\
Min:\t\t{minTemperature:.1f} {degree}C\n\
Humidity:\t{humidity} %\n\
Wind:\t\t{wind} km/h\n')

print(f'It feels like {feelsLike:.1f} {degree}C and there will be {weatherDescription}.')
sleep(10)