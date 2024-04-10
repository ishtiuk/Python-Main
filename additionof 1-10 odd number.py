import pyttsx3

math = 0
i = 1

hxd_bot = pyttsx3.init()
while i <= 10:
    if i%2 != 0:
        math = math + i
        print(math)
        hxd_bot.say(math)
        hxd_bot.runAndWait()
    i += 1 
    #i += 1 or i = i + 1 is same thing