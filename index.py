# importing speechToText
from speechToText import *

# importer Yake, keyword extractor
import yake 

# caller speechToText
speechToText()

# ---------------henter ut keywords---------------

f = open('input.txt', 'r')

yrnøkkelord = ['weather', 'forecast']
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(f.read())

""" for keywords in nøkkelord:
    print(keywords)
    #calle spotify """
while (1):
    if keywords in yrnøkkelord:
        print('yo')
        #calle yr
    
    

# --------------------operere basert på keywords--------------------

    # -----------------Værmelding fra YR-----------------
def weatherForecast():
    return

    # -------------------Spotify-------------------


    # -------------------Klokka-------------------


# Printe resultat i output.txt# Importer dvs. API for funksjonalitet