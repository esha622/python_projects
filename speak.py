import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    

    voices = engine.getProperty('voices')
    

    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - ID: {voice.id}")


    female_voice_index = 1
    engine.setProperty('voice', voices[female_voice_index].id)
    

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)

    engine.say(text)
    engine.runAndWait()

speak("Hello, how can I assist you today?")