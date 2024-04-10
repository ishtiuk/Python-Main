import pyttsx3
math = 0
i = 1
hxd_bot = pyttsx3.init()

while i <= 10:
    math = math + i
    i = i + 1
#  or i += 1
    print(math)
    hxd_bot.say(math)
    hxd_bot.runAndWait()
