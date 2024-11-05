# importing speechToText
from speechToText import *

# caller speechToText
speechToText()


# importer Yake, keyword extractor
import yake 

f = open('input.txt', 'r')

nøkkelord = ['weather', 'spotify']
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(f.read())

for keywords in nøkkelord:
    print(keywords)
    
    
# henter ut keywords


# operere basert på keywords

    # Værmelding fra YR

    # Spotify


# Printe resultat i output.txt# Importer dvs. API for funksjonalitet