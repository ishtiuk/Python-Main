import pyttsx3
from playsound import playsound

hxd_bot = pyttsx3.init()
rate = hxd_bot.getProperty("rate")
hxd_bot.setProperty("rate", 180)
print(rate)

#setting up volume between 0 or 1
volume = hxd_bot.getProperty("volume")
print("volume is {0}".format(volume))

#changing default volumne
hxd_bot.setProperty("volumn", 2)
voices = hxd_bot.getProperty("voices")

#male voice's index 0 and female voice's index is 1
print("Female Voice : {0}".format(voices[1].id))
print("Male Voice: {0}".format(voices[0].id))

#setting up voice
hxd_bot.setProperty("voice", voices[1].id)
# hxd_bot.say("Hi, I'm Alexa. Your virtual Assistant.")
# hxd_bot.say("how can I help?")
# hxd_bot.runAndWait()
'''hxd_bot.say("Hey, I'm Alexa. Your virtual assistant. How can I help?")
hxd_bot.runAndWait()
x = input()
if x == "who are you":
    hxd_bot.say("I'm a virtual bot, named Alexa. I made by hxd agency")
    hxd_bot.runAndWait()'''
pwd = '1139'
playsound('D:\\pyaudio file\\Binary_Code_effects_example(128k)-2.mp3')
hxd_bot.say("Please enter authentication password ")
hxd_bot.runAndWait()
pd = input("Please enter authentication password: ")

if pd == pwd:
    playsound('D:\\pyaudio file\\Access_Granted(128k).mp3')
    hxd_bot.say("Welcome Sir, to HxD Corpo. ")
    hxd_bot.say("activating all corporational facilities.")
    hxd_bot.say("activating database")
    hxd_bot.runAndWait()
    hxd_bot.say("Do you want a namta?")
    hxd_bot.runAndWait()

    s = input("Enter number: ")
    sum = int(s)
    i = 1
    while i <= 10:
        sum = sum + i
        i += 1 
    print(sum)
        
        # if i == 8:
        #     break
        #i = i + 1 or i += 1 is same thing
    
else:
    playsound('D:\\pyaudio file\\Access_Denied_-_Sound_Effect_(HD)(128k).mp3')
    hxd_bot.say("Deactivating all services!Closing database")
    hxd_bot.runAndWait()
    playsound('D:\\pyaudio file\\Binary_Code_sound_effects_example(128k).mp3')
