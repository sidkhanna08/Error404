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
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id,'rate',150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

flag=0
def take_cmd():
    try:
        with sr.Microphone() as source:
            audio = recorder.listen(source)
            audio_cmd = recorder.recognize_google(audio)
            audio_cmd = audio_cmd.lower()
            audio_cmd1 = audio_cmd
            if (audio_cmd=='hey siri'):
                talk("ummm hmmm.....")
                print("ummm hmmm.....")
            elif 'hey siri' in audio_cmd:
                talk(audio_cmd1.replace("hey siri",""))
                print(audio_cmd1)
                flag=1
            elif (audio_cmd=='hey siri i love you'):
                talk("i love you too sid")
                print("i love you too sid")

    except:
        pass
    return audio_cmd

def run_siri():
    if (flag==1):
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
        # elif 'open' in command:
        #     command= command.replace('open',"")
        #     subprocess.Popen('C)
        else :
            talk('Please say the command again')

while True:
    run_siri()