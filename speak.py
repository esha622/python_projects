import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Get the list of available voices
    voices = engine.getProperty('voices')
    
    # Print available voices for selection
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - ID: {voice.id}")

    # Set the voice to the identified female voice index
    female_voice_index = 1  # Adjust this index based on your findings
    engine.setProperty('voice', voices[female_voice_index].id)
    
    # Adjust the speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello, how can I assist you today?")