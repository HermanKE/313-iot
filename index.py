# importing speechToText
from speechToText import *
import keyboard
# importer Yake, keyword extractor
import yake 

# caller speechToText, Må adde en type break så den ikke kjører uendelig.
while keyboard.add_hotkey('space')
    speechToText()


# ---------------henter ut keywords---------------

f = open('input.txt', 'r')

yrNøkkelord = ['weather', 'forecast']
spotifyNøkkelord = ['spotify', 'play', 'artist', 'music']

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(f.read())

for keyword, score in keywords:
    if keyword in yrNøkkelord:
        print("Hello world")
        break
    elif keyword in spotifyNøkkelord:
        print('yo')
        # Call the relevant function or execute the relevant code here
        break  
    
    

# --------------------operere basert på keywords--------------------

    # -----------------Værmelding fra YR-----------------
def weatherForecast():
    return

    # -------------------Spotify-------------------


    # -------------------Klokka-------------------


# Printe resultat i output.txt# Importer dvs. API for funksjonalitet