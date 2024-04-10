import pyttsx3

annocher_bot = pyttsx3.init()

voices = annocher_bot.getProperty('voices')
annocher_bot.setProperty('voice', voices[0].id)

rate = annocher_bot.getProperty('rate')
annocher_bot.setProperty('rate', 190)

def talker(str):
    annocher_bot.say(str)
    annocher_bot.runAndWait()

def rock_paper_scaissor(p1, p2):
    if p1 == p2:
        talker("It's a tie, try again")
        print("It's a tie, try again")

    elif p1 == 'rock':
        if p2 == 'scissors':
            talker('first player wins')
            print('first player wins')
        elif p2 == 'paper':
            talker('second player wins')
            print('second player wins')
        else:
            talker("invalid selection, try again")
            print("invalid seletion, try again")

    elif p1 == 'paper':
        if p2 == 'rock':
            talker('first player wins')
            print('first player wins')
            
        elif p2 == 'scissors':
            talker('second player wins')
            print('second player wins')  
        else:
            talker("invalid selection, try again")
            print("invalid seletion, try again")

    elif p1 == 'scissors':
        if p2 == 'paper':
            talker('first player wins')
            print('first player wins')
        elif p2 == 'rock':
            talker('second player wins')
            print('second player wins')  
        else:
            talker("invalid selection, try again")
            print("invalid seletion, try again")

    else:
        talker("trouble occured, gameover. try again next time")
        print("trouble occured, gameover")

talker('choose one from, rock, paper or scissors')
p1 = input("|| Choose onething among:  rock ,  paper or scissors || Player 1 : ")
p2 = input("|| Choose onething among:  rock ,  paper or scissors || Player 2 : ")


rock_paper_scaissor(p1, p2)