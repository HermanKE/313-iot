# Importer dvs. API for funksjonalitet
import yake 

f = open('input.txt', 'r')

nøkkelord = ['været', 'spotify']
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(f.read())

for kw in keywords:
    print(kw)