import pyttsx3
hari = pyttsx3.init()
a = input("Say Something : ")
hari.say(a)
hari.runAndWait()
