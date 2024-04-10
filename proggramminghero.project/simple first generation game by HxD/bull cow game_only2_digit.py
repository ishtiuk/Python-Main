import random
import pyttsx3

talking_bot = pyttsx3.init()

voice = talking_bot.getProperty('voices')
talking_bot.setProperty('voice', voice[0].id)

rate = talking_bot.getProperty('rate')
talking_bot.setProperty('rate', 192)

talking_bot.say("welcome to HxD cyber paradise")
talking_bot.runAndWait()

def game_annoucher(str):
    talking_bot.say(str)
    talking_bot.runAndWait()

def bull_cow_game():
    
    secret_random_numb = str(85)

    remain_trail = 5    

    while True:
        user_inp = str(input("\n::: Enter a random number here ::: > "))
        if secret_random_numb == user_inp:
            print('|| congrats! you have guesed the number correctly, you won the game ||')
            game_annoucher("congrats you have won the game")
            break
        
        if len(secret_random_numb) != len(user_inp):
            print('|| Invalid Selection, make sure that the number contains 2 digits only ||')
            game_annoucher('Invalid Selection, make sure that the number contains 2 digits only')
            break

        elif len(secret_random_numb) == len(user_inp):
            bull = 0
            cow = 0
            if secret_random_numb[0] == user_inp[0]:
                bull = bull + 1
            if secret_random_numb[1] == user_inp[1]:
                bull = bull + 1
            if secret_random_numb[0] == user_inp[1]:
                cow = cow + 1
            if secret_random_numb[1] == user_inp[0]:
                cow = cow + 1

            remain_trail -= 1

            print("|| bull occupied: ", bull, '||')
            print("|| cow occupied: ", cow, '||')

            if remain_trail ==  0:
                print("|| you have lost the game ||")
                game_annoucher('sorry, you have lost the game')
                break

bull_cow_game()
print('\n|| All right deserved to ||\n|| Game development credit for HxD developers ||\n::: HxD Corporation :::\n')