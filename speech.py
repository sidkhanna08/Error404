import speech_recognition as sr
import pyaudio
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
import subprocess

recorder = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_cmd():
    try:
        with sr.Microphone() as source:

            audio = recorder.listen(source)
            audio_cmd = recorder.recognize_google(audio)
            audio_cmd = audio_cmd.lower()
            audio_cmd1 = audio_cmd
            if (audio_cmd=='hi melody'):
                talk('ummm hmmm.....')
                print('ummm hmmm.....')

            elif 'hi melody' in audio_cmd:
                talk(audio_cmd1.replace('hi melody',''))
                print(audio_cmd1)

            elif (audio_cmd=='hi melody i love you'):
                talk('i love you too sid')
                print('i love you too sid')

    except:
        pass

    return audio_cmd

def main():
    command = take_cmd()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time )

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'what' in command:
        info = wikipedia.summary(command,2)
        talk(info)
        pywhatkit.search(command)

    elif 'open calculator' in command:
        command= command.replace('open',"")
        subprocess.Popen("C:\Windows\System32\calc.exe")

    elif 'open notepad' in command:
        command=command.replace('open notepad and type',"")
        # subprocess.Popen("C:\Windows\System32\notepad.exe")
        with open('new.txt','w') as g:
            g.write(command)

    else:
        talk('how can i help you')

main()

