import pyttsx3
hxd_bot = pyttsx3.init()
# Q =  ['what is this', , 'what is?', ,  ]
A = ["HxD_bot: I'm HxD bot", "HxD_bot: It is a bot which answers the clients"]
print("Have you any question?")
question_input = input()

for a in A:
    if question_input == 'what is this' and 'what this' and 'who are you?':
        print
        print
        print(A[0])
        print
        hxd_bot.say("I'm HxD bot")
        hxd_bot.runAndWait()
        break
    elif question_input == 'what is hxd' and 'what is' and 'what is HxD?':
        print
        print
        print(A[1])
        print
        hxd_bot.say("It is a bot which answers the clients")
        hxd_bot.runAndWait()
        break
    else:
        print("error question")
        break