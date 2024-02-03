import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    #engine.say('Hello! Mister Arnab')
    #engine.say('Boss! How can I help you!')
    print("listening")
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #talk(command)

    except:
        pass

    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song+' enjoy')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk('The time now is'+time)

    elif 'tell me about' in command:
        search = command.replace("tell me about","")
        info = wikipedia.summary(search) 
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'love' in command:
        talk("No, you have a girlfriend")

    else:
        talk("I didn't get it! Let me search it on Google")
        pywhatkit.search(command)

    

        

talk("Hello Arnab")
print("I am ready to serve you!")

while True:
    run_alexa()