# importing speechToText
from speechToText import *
import keyboard
import yake 
import datetime

# caller speechToText, Må adde en type break så den ikke kjører uendelig.
#speechToText()
#Denne har ingen exit funksjonalitet, så vil bare loope for alltid, må se om det er mulig og gi den exit og av og på knapp


# ---------------henter ut keywords---------------

i = open('input.txt', 'r')
o = open('output.txt', 'w')


yrNøkkelord = ['weather', 'forecast']
spotifyNøkkelord = ['spotify', 'play', 'artist', 'music']
clockNøkkelord = ['time', 'clock']
locationNøkkelord = []

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(i.read())
# --------------------operere basert på keywords--------------------

    # -----------------Værmelding fra YR-----------------
def weatherForecast():
    return

    # -------------------Spotify-------------------


    # -------------------Klokka-------------------
def CurrentTime():
    currentTime = str(datetime.datetime.now())
    o.write("The current time is " + currentTime)
    o.close()
    return

# Printe resultat i output.txt# Importer dvs. API for funksjonalitet

for keyword, score in keywords:
    if keyword in yrNøkkelord:
        print("Hello world")
        break

    elif keyword in spotifyNøkkelord:
        print('yo')
        # Spotify api
        break

    elif keyword in locationNøkkelord:
        # Veibilde / direcions
        break

    elif keyword in clockNøkkelord:
        CurrentTime()
        break