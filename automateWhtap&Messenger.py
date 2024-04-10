import pyautogui
import time
message_count = 0

# while message_count <= 10:
# to send message for specific iteration
def auto_typer(sentence):   
    while True:
        time.sleep(1)
        pyautogui.typewrite(sentence)
    # time.sleep(2)
    # to sleep after type
    # to look like the bot as natural
    # _________________
        pyautogui.press('enter')

    # message_count += 1

auto_typer(input("Enter sentence, Sir: "))
