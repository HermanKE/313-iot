# importing speechToText
from speechToText import *
import keyboard
import yake
import datetime
import pygame
import random
import googlemaps


# API key til google maps
gmaps = googlemaps.Client(key='AIzaSyCc8wAa6p-IMlpXjxXvcRJS0cI9VCJrsfQ')


# caller speechToText, Må adde en type break så den ikke kjører uendelig.
#speechToText()
#Denne har ingen exit funksjonalitet, så vil bare loope for alltid, må se om det er mulig og gi den exit og av og på knapp


# ---------------henter ut keywords---------------

i = open('input.txt', 'r')
o = open('output.txt', 'w')

path = '' # dette vil bli endret til der mappen med sangen ligger
music_files = ['ex1.mp3', 'ex2.mp3', 'ex3.mp3']

yrNøkkelord = ['weather', 'forecast']
clockNøkkelord = ['time', 'clock', 'date']
locationNøkkelord = ['traffic'], ['city'], ['drive']
musikkNøkkelord = ['play', 'artist', 'music']

pygame.mixer.init()

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(i.read())
# --------------------operere basert på keywords--------------------

    # -----------------Værmelding fra YR-----------------
def weatherForecast():
    return

    # -------------------Spotify-------------------
def playMusic():
    pygame.mixer.music.load(path + music_files[random.choice(music_files)])
            

    # -------------------Klokka-------------------
def CurrentTime():
    currentTime = str(datetime.datetime.now())
    o.write("The current time is " + currentTime)
    o.close()
    return

    # -------------------Sjekke trafikk-------------------
def check_traffic():
    origin = "Gyldenløves gate 9, 4611 Kristiansand"
    destination = "Campus Kristiansand, Universitetsveien 25, 4630 Kristiansand"
    now = datetime.datetime.now()#default sted og tid
    # forespørsel om trafikk data fra Google Maps
    directions = gmaps.directions(origin, destination, mode="driving", departure_time=now, traffic_model="best_guess") #2 oblig parametre, defualt driving mode for directions, avgang nå for live oppdateringer, best_guess som nøytral defualt 
    estimation = directions[0]['legs'][0]['duration_in_traffic']['text'] #kun 1 rute, 1 lengde(leg), duration gir tidsestimering for leggen, text gjør duration om til string fremfor abs verdi
    print(f"Travel time with traffic: {estimation}")
    return estimation



# Printe resultat i output.txt# Importer dvs. API for funksjonalitet

for keyword, score in keywords:
    if keyword in musikkNøkkelord:
        print('sanger:')
        # Then check for genre-specific words
        playMusic()

    
    elif keyword in yrNøkkelord:
        print("Hello world")
        break

    elif keyword in locationNøkkelord:
        print("Hello world")
        check_traffic()
       

    elif keyword in clockNøkkelord:
        CurrentTime()
        break

