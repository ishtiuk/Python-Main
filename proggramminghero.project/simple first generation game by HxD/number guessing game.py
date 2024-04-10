import random
import pyttsx3

score = 0
game_annoucher_bot = pyttsx3.init()

voices = game_annoucher_bot.getProperty('voices')
game_annoucher_bot.setProperty('voice', voices[0].id)

rate = game_annoucher_bot.getProperty('rate')
game_annoucher_bot.setProperty('rate', 200)

def talker(str):
    game_annoucher_bot.say(str)
    game_annoucher_bot.runAndWait()

talker(" Guses a random number between 1 to 10 and enter that. or enter 'q' to exit anytime")
    
while True:
    random_numb = random.randint(1,3)

    
    user = input("Guess a random number between 1 to 10, to play || or enter 'q' to exit anytime: ")
    if user == 'q':
        print("exiting, gameover")
        talker('trouble to run algorithom, gameover')
        break
   
    user_numb = int(user)

    if user_numb == random_numb:
        print("congrats you guessed it correctly")
        score += 10
        score_talk_str = "congrats you guessed it correctly, now your score is "+str(score)
        talker(score_talk_str)
        print("Now your score is: ", score)
    

    else:
        right_score_talker = "guess didn't match, the right number is " + str(random_numb)
        talker(right_score_talker)
        print('sorry, your guess is incorrect. the number right number is: ', str(random_numb))

    
   
