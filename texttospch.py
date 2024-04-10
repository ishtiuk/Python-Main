import pyttsx3

hxd_friend = pyttsx3.init()

b = input()
if b == "Jarvis":
    hxd_friend.say('''Hi, I'm Jarvis.
    your virtual assistant.
    how can I help?''')
hxd_friend.runAndWait()
    