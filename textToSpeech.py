import pyttsx3
import asyncio

def textToSpeech():
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Optional: Adjust TTS properties (rate, volume, etc.)
    engine.setProperty('rate', 120)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Open the file with the text to read aloud
    with open("output.txt", "r") as file:
        text = file.read().strip()
        print(f"Text to speak: {text}")  # Debug: Confirm the text is complete

    # Break the text into smaller chunks if it's too long
    for line in text.split('. '):  # Split into sentences by '. '
        engine.say(line.strip())  # Speak each sentence
        engine.runAndWait()  # Wait for the sentence to complete before starting the next

    # Stop the engine properly
    engine.stop()


#def textToSpeech():
#    with open('output.txt', 'r') as o:  # Using 'with' to handle file closing automatically
#       content = o.read()  # Read the entire file content into a string
#    engine = pyttsx3.init()
#    engine.say(content)  # Pass the text content to engine.say()
#    engine.runAndWait()  # Run the speech engine to speak the text

# Call the function
#textToSpeech()
