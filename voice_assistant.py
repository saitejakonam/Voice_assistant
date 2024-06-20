import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query

if __name__ == '__main__':

    speak("Amigo assistant activated")
    speak("How can I help you?")
    while True:
        query = take_command().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find information on Wikipedia.")
        
        elif 'who are you' in query:
            speak("I am Amigo, developed by Jaspreet Singh.")
        
        elif 'open' in query:
            if 'youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("youtube.com")
            elif 'google' in query:
                speak("Opening Google")
                webbrowser.open("google.com")
            elif 'github' in query:
                speak("Opening GitHub")
                webbrowser.open("github.com")
            elif 'stack overflow' in query:
                speak("Opening Stack Overflow")
                webbrowser.open("stackoverflow.com")
            elif 'spotify' in query:
                speak("Opening Spotify")
                webbrowser.open("spotify.com")
            elif 'whatsapp' in query:
                speak("Opening WhatsApp")
                loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(loc)
            elif 'local disk c' in query:
                speak("Opening Local Disk C")
                webbrowser.open("C://")
            elif 'local disk d' in query:
                speak("Opening Local Disk D")
                webbrowser.open("D://")
            elif 'local disk e' in query:
                speak("Opening Local Disk E")
                webbrowser.open("E://")
            elif 'facebook' in query:
                speak("Opening Facebook")
                webbrowser.open("facebook.com")
            elif 'twitter' in query:
                speak("Opening Twitter")
                webbrowser.open("twitter.com")
            elif 'gmail' in query:
                speak("Opening Gmail")
                webbrowser.open("mail.google.com")
            elif 'amazon' in query:
                speak("Opening Amazon")
                webbrowser.open("amazon.com")
            elif 'instagram' in query:
                speak("Opening Instagram")
                webbrowser.open("instagram.com")
            elif 'linkedin' in query:
                speak("Opening LinkedIn")
                webbrowser.open("linkedin.com")
            elif 'pinterest' in query:
                speak("Opening Pinterest")
                webbrowser.open("pinterest.com")
            elif 'reddit' in query:
                speak("Opening Reddit")
                webbrowser.open("reddit.com")
            elif 'bbc news' in query:
                speak("Opening BBC News")
                webbrowser.open("bbc.com")
            elif 'cnn' in query:
                speak("Opening CNN")
                webbrowser.open("cnn.com")
            elif 'whatsapp web' in query:
                speak("Opening WhatsApp Web")
                webbrowser.open("web.whatsapp.com")
            elif 'google maps' in query:
                speak("Opening Google Maps")
                webbrowser.open("maps.google.com")
            elif 'google drive' in query:
                speak("Opening Google Drive")
                webbrowser.open("drive.google.com")
            elif 'google photos' in query:
                speak("Opening Google Photos")
                webbrowser.open("photos.google.com")
            elif 'google docs' in query:
                speak("Opening Google Docs")
                webbrowser.open("docs.google.com")
            elif 'google sheets' in query:
                speak("Opening Google Sheets")
                webbrowser.open("sheets.google.com")
            elif 'google slides' in query:
                speak("Opening Google Slides")
                webbrowser.open("slides.google.com")
            elif 'onedrive' in query:
                speak("Opening OneDrive")
                webbrowser.open("onedrive.com")
            elif 'dropbox' in query:
                speak("Opening Dropbox")
                webbrowser.open("dropbox.com")
            elif 'microsoft teams' in query:
                speak("Opening Microsoft Teams")
                webbrowser.open("teams.microsoft.com")
            elif 'skype' in query:
                speak("Opening Skype")
                webbrowser.open("skype.com")
            elif 'zoom' in query:
                speak("Opening Zoom")
                webbrowser.open("zoom.us")
            elif 'microsoft word' in query:
                speak("Opening Microsoft Word")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            elif 'microsoft excel' in query:
                speak("Opening Microsoft Excel")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            elif 'microsoft powerpoint' in query:
                speak("Opening Microsoft PowerPoint")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            elif 'outlook' in query:
                speak("Opening Outlook")
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
            elif 'thunderbird' in query:
                speak("Opening Thunderbird")
                os.startfile("C:\\Program Files\\Mozilla Thunderbird\\thunderbird.exe")
            elif 'safari' in query:
                speak("Opening Safari")
                webbrowser.open("safari.com")
            elif 'mozilla firefox' in query:
                speak("Opening Mozilla Firefox")
                webbrowser.open("firefox.com")
            elif 'opera' in query:
                speak("Opening Opera")
                webbrowser.open("opera.com")
            elif 'brave browser' in query:
                speak("Opening Brave Browser")
                webbrowser.open("brave.com")
            elif 'itunes' in query:
                speak("Opening iTunes")
                os.startfile("C:\\Program Files\\iTunes\\iTunes.exe")
            elif 'vlc media player' in query:
                speak("Opening VLC Media Player")
                os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
            elif 'windows media player' in query:
                speak("Opening Windows Media Player")
                os.startfile("C:\\Program Files\\Windows Media Player\\wmplayer.exe")
            elif 'realplayer' in query:
                speak("Opening RealPlayer")
                os.startfile("C:\\Program Files\\Real\\RealPlayer\\realplay.exe")
            elif 'quicktime player' in query:
                speak("Opening QuickTime Player")
                os.startfile("C:\\Program Files\\QuickTime\\QuickTimePlayer.exe")
            elif 'adobe reader' in query:
                speak("Opening Adobe Reader")
                os.startfile("C:\\Program Files\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe")
            elif 'notepad' in query:
                speak("Opening Notepad")
                os.startfile("notepad.exe")
            elif 'wordpad' in query:
                speak("Opening WordPad")
                os.startfile("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")
            elif 'paint' in query:
                speak("Opening Paint")
                os.startfile("mspaint.exe")
            elif 'calculator' in query:
                speak("Opening Calculator")
                os.startfile("calc.exe")
            elif 'command prompt' in query:
                speak("Opening Command Prompt")
                os.startfile("cmd.exe")
            elif 'control panel' in query:
                speak("Opening Control Panel")
                os.startfile("control.exe")
            elif 'task manager' in query:
                speak("Opening Task Manager")
                os.startfile("taskmgr.exe")
            elif 'sleep' in query:
                speak("Goodbye!")
                exit(0)
            else:
                speak("Sorry, I couldn't understand the command.")
