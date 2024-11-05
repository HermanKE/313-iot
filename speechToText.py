# Importerer libraries/pakker
import speech_recognition as sr
import pyttsx3

#funksjon som kan calles fra Index.py
def speechToText():

    # Initialisere recognizer
    r = sr.Recognizer()

    # Funksjon som tar opp lyd fra bruker
    def record_text():
        # Loop i tilfelle det blir errors
        while(1):
            try:
                # Bruker mikrofonen som kilde for input
                with sr.Microphone() as mic:
                    # Forbreder recognizer til å motta input
                    r.adjust_for_ambient_noise(mic, duration=0.2)

                    # Hører etter brukers input
                    userAudio = r.listen(mic)

                    # Bruker google til å gjennkjenne audio
                    requestText = r.recognize_google(userAudio, language="EN-gb") # definere norsk språk

                    return requestText

            # Feilmeldinger:
            # Feil oppstod under request til Google
            except sr.RequestError as e:
                print("Kunne ikke requeste resutatet; {0}".format(e))

            # Skjønner ikke hva brukeren sa
            except sr.UnknownValueError:
                print("Cannot understand you, speak clearly. :)")

        return

    # Funksjon som tømmer input.txt
    def clear_text():
        f = open("input.txt", "w") 
        f.close()

        return  
    
    # Funksjon som lager input.txt og skriver i den
    def input_text(text):
        f = open("input.txt", "a") # Lager en input-fil
        f.write(text) # Skriver tekst
        f.write("\n") # Ny linje
        f.close()

        return

    # Kjører funksjonen som tømmer input.txt
    clear_text() 

    # Loop som recorder og skriver tekst i input.txt
    # While(1) skal endres til buttonPress
    while(1):
        text = record_text()
        input_text(text)

        print("Wrote text")

