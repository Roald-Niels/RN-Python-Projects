import requests
import os
import sys

api_key = '1d413f67a4a3bcb61485fc8828bc7a2b'

print("Welcome to Request Weahter!")
print("To find out what the weather is like")

user_input = input("Please enter your zip code: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("Sorry, your location is not Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    windspeed = weather_data.json()['wind']['speed']
    
    print(f"The weather in the zip code area {user_input} is: {weather}")
    print(f"The temperature in zip code area {user_input} is: {temp}ºF")
    print(f"The wind speed in zip code area {user_input} is: {windspeed} mph")

restart = input("Would you like to pull up a different area? press y to restart or n to quit ")

if restart == "y":
  os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

elif restart == "n":
  sys.exit(0)
