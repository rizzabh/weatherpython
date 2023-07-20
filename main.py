from gtts import gTTS
import requests
import json
# import win32com.client
import os
name = input("Hello, Im WeatherBot,Whats your name\n (After giving your name please open hello2.mp3)\n ")
tts = gTTS(text=f"Hello {name}, I hope you're fine. Can you provide name of the city so that i can provide Weather "
                f"details on the next command")
tts.save("hello2.mp3")
city = input("Enter a city name\n (After giving city name please open weather.mp3)\n")
url = f"https://api.weatherapi.com/v1/current.json?key=d84d86f51b5845b7bed174046231707&q={city}"
r = requests.get(url)
# print(r.text)
w = json.loads(r.text)
currentWeather = w["current"]["temp_c"]
condition = w["current"]["condition"]["text"]
print(currentWeather)
print(condition)
c = f"it seems like its gonna be {condition} today Take care"

tts = gTTS(text=f"Hello {name} the realtime weather in {city} is {currentWeather} degrees. {c}", lang="en")
tts.save("Weather.mp3")

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# os.system(f"say 'The current weather in {city} is {w} degrees")




