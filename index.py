# importing speechToText
import os
from speechToText import *
from textToSpeech import *
import keyboard
import yake
import datetime
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time
import python_weather
import asyncio


i = open('input.txt', 'r')
o = open('output.txt', 'w')
o.close()
o = open("output.txt", "w")

# caller speechToText, Må adde en type break så den ikke kjører uendelig.
speechToText()
#Denne har ingen exit funksjonalitet, så vil bare loope for alltid, må se om det er mulig og gi den exit og av og på knapp


# ---------------henter ut keywords---------------



path = './mp3/' # dette vil bli endret til der mappen med sangen ligger
music_files = ['Rick Astley - Never Gonna Give You Up.mp3', 'Backstreet Boys - I Want It That Way.mp3', 'Oliver Cheatham - Get Down Saturday Night.mp3']


yrNøkkelord = ['weather', 'forecast']
clockNøkkelord = ['time', 'clock', 'date']
locationNøkkelord = []
musikkNøkkelord = ['play', 'artist', 'music']
Stop = ['stop', 'Stop']






kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(i.read())
# --------------------operere basert på keywords--------------------


# -----------------Weather Forecast-----------------
async def weatherForecast() -> None:
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client() as client:
        # fetch a weather forecast from a city
        weather = await client.get('Kristiansand')
    
        # get the weather forecast for a few days
        print('The weather forecast for today and the next two days')
        for daily in weather:
            """ print(daily.date)
            print('The weather will be', weather.kind)
            print('The temperature will be', daily.temperature, 'C')
            print('The wind speeds will be', weather.wind_speed, 'kph')
            print('Sunrise:', daily.sunrise)
            print('Sunset:', daily.sunset)
            print('') """

            o.write(str(daily.date) + '\n')  # Convert datetime.date to string and add newline
            o.write('The weather will be ' + str(weather.kind) + '\n')
            o.write('The temperature will be ' + str(daily.temperature) + ' Celsius\n')
            o.write('The wind speeds will be ' + str(weather.wind_speed) + ' kilometers per hour\n')
            o.write('Sunrise will be at: ' + str(daily.sunrise) + '\n')
            o.write('Sunset will be at: ' + str(daily.sunset) + '\n')
            o.write('\n')

    # -------------------Play music-------------------
def playMusic():
    pygame.init()  # Initialize pygame
    pygame.mixer.init()
    
    # Select a random song from the list
    selected_song = random.choice(music_files)
    full_path = os.path.join(path, selected_song)
    
    try:
        pygame.mixer.music.load(full_path)
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
        
        print(f"Now playing: {selected_song}")
        
        # Keep the program running until the music stops
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error as e:
        print("Error loading or playing the music:", e)
            

    # -------------------Klokka-------------------
def CurrentTime():
    currentTime = str(datetime.datetime.now())
    o.write("The current time is " + currentTime)
    o.close()
    return

# Printe resultat i output.txt# Importer dvs. API for funksjonalitet

for keyword, score in keywords:
    if keyword in musikkNøkkelord:
        print('Get jiggy')
        # Then check for genre-specific words
        playMusic()

    
    elif keyword in yrNøkkelord:
        asyncio.run(weatherForecast())
        break

    elif keyword in locationNøkkelord:
        # Veibilde / direcions
        break

    elif keyword in clockNøkkelord:
        CurrentTime()
        break

asyncio.run(textToSpeech())