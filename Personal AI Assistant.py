import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[0].id)



def talk(text):
    alexa.say(text)
    alexa.runAndWait()



def take_command():
    
    
    try:
        with sr.Microphone() as source:
            print("listening")

            voice = listener.listen(source)
           
           
            command = listener.recognize_google(voice)
            #talk(command)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

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
        command = command.replace('tell me a joke', '')

    elif 'love' in command:
        talk("No, you have a girlfriend")
        command = command.replace('do you love me', '')

    else:
        talk("I didn't get it! Let me search it on Google")
        pywhatkit.search(command)

talk("Hello")
print("I am ready to serve you!")
talk("What can I do for you!")

while True:
    run_alexa()
   