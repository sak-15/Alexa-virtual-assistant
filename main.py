import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_alexa():

    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is" + time)

    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is ' in command:
        thing = command.replace('what is', '')
        summ = wikipedia.summary(thing, 2)
        print(summ)
        talk(summ)

    elif 'hello' in command:
        talk('hello smarty')

    elif 'what is your name' in command:
        talk('my name is humpty')

    elif 'i love you' in command:
        talk('i love you too')

    elif 'joke' in command:
        talk(pyjokes.get_jokes())

    else:
        talk('please say again')


while True:
    run_alexa()