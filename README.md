# 313-iot
IoT prosjekt i IS-313, 5. semester

Formålet med dette prosjektet er å lage en AI-assistent som fungerer i samarbeid med en Rasberry PI 4. Denne assistenten bruker tale-til-tekst og talgjenkjenningsteknologier, for å kunne kommunisere med brukeren på en brukervennlig måte. Hovedkomponentene i denne assistenten er Rasberry PI, en mikrofon, en høyttaler, et display, og et program som inneholder nødvendig kode. Målet med assistenten er å gjennomføre hverdagslige oppgaver som en bruker ofte er borti. Hovedfunksjonene som vi ønsket å integrere i assistenten først og fremst er sjekk og tilbakemelding av tid, været, og trafikk i sanntid, samt mulighet for å spille musikk ved forespørsel. 


## speechToText.py
Skal plukke opp lyd, etter knappetrykk, og skrives inn i tekstfil

10.28 - Språket skal være engelsk

Program som gjør tale om til tekst og skriver det inn i input.txt
  ### speechToText()
  Bruker speechrecognition libarry til å plukke opp audio, og hvis mulig gjør det om til tekst.
  Bruker også threads library, så man kan avslutte funksjonen med et tastetrykk ettersom den lytter i en uendelig loop.


## index.py
Inneholder hovedfunksjonene som skal dannne svar basert på teksten fra speechToText.py

Filen inneholder alle funksjonene til programmet, og det er her alle pakkene som trenges til funksjonene er importert. Funksjonene i index.py som kjører når de bestemte nøkkelordene er oppfattet i speechToText er:
### weatherForecast()
Henter værmeldingen for Kristiansand for i dag og de to neste dagene, og skriver den i output.txt

### playMusic()
Velger en tilfeldig sang fra mappen mp3, og spiller av den til sangen er ferdig eller tasten “q” blir trykket ned i et halvt sekund

### CurrentTime()
Henter nåværende tid, og skriver den i output.txt


### check_traffic()
Startpunkt er satt til UiA Kristiansand, Sluttpunkt er satt til UiA Grimstad. Bruker google maps til å finne estimert tid det tar å kjøre mellom start- og sluttpunkt. Og skriver den i output.txt

### for keyword, score in keywords:
En for-løkke som sjekker om bestemte nøkkelord er fanget opp og skrevet i input.txt. Den trigger så riktig funksjon (av de ovenfor) basert på if-setningen inne i for-løkka.


## textToSpeech.py
Skal gjøre svartekst fra index om til lyd og et svar.
Program som inneholder funksjonen som gjør at innholdet i output.txt blir gjort om til audio.
### textToSpeech()
Åpner output.txt og leser ut alt innhold.



## input.txt
Fil som blir skrevet i basert på tale fra brukeren.

## output.txt
Fil som blir skrevet i av de forskjellige funksjonene i index.py.

## readme.md
Readme inneholder informasjon om programmet.

## .gitignore
Gjør at git ignorerer filer vi ikke ønsker skal bli med i repositoriet. Ignorerer .txt og .pyc.

## mappe med mp3
Bare en mappe som inneholder mp3 filer som skal spilles av hvis man ber om musikk.
