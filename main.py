import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com") 
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com") 
   elif "open instagram" in c.lower():
      webbrowser.open("https://instagram.com")  
   elif "open linedin" in c.lower():
      webbrowser.open("https://linkedin.com")       
   elif c.lower().startswith("play"):
       song=c.lower().split(" ")[1]
       musicLibrary.music[song]
       link=musicLibrary.music[song]
       webbrowser.open(link)  
   else:
      pass        

if __name__ == "__main__":
    speak("Initialising Jarvis......")
    while True:
        r = sr.Recognizer()
      
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
              print("Listening")
              audio = r.listen(source,timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower():

                speak("Ya")
                with sr.Microphone() as source:
                 print("Jarvis active")
                 audio = r.listen(source)
                    
                 command = r.recognize_google(audio)

                 processCommand(command)

           
        except Exception as e:
            print("Google error; {0}".format(e))
