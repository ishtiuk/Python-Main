# import random

secret_num = str(85)
remaining = 5

def user_creditials(usr_guess, secret_num):
    bulls_cows = [0, 0]
    for i in range(len(secret_num)):
        if usr_guess[i] == secret_num[i]:
            bulls_cows[0] += 1
        elif usr_guess[i] in secret_num:
            bulls_cows[1] += 1
        
    return bulls_cows

# def main():
while remaining > 0:
    player_guess = input("Enter a number: ")

    if player_guess == secret_num:
        print("Yay, you guessed it correctly!")
        print("YOu Win")
        
    if len(player_guess) != len(secret_num):
        print('''invalid number, 
        make sure that ''')

    elif len(player_guess) == len(secret_num):
        bullcows = user_creditials(player_guess, secret_num)
        bulls = bullcows[0]
        cows = bullcows[1]
        print('bulls:',bulls)
        print('cows:',cows)

        remaining -= 1

        if remaining < 1:
            print("Sorry, you have lost the game")
            break


