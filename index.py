# Importer dvs. API for funksjonalitet
import yake 

f = open('input.txt', 'r')

nøkkelord = ['weather', 'spotify']
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(f.read())

for keywords in nøkkelord:
    print(keywords)