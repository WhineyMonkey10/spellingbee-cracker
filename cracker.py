#Cracker
import pyautogui
import time

w1 = input("Enter the first letter: ")
w2 = input("Enter the second letter: ")
w3 = input("Enter the third letter: ")
w4 = input("Enter the fourth letter: ")
w5 = input("Enter the fifth letter: ")
w6 = input("Enter the sixth letter: ")
w7 = input("Enter the center letter: ")

ws = set([w1, w2, w3, w4, w5, w6, w7])
print(ws)

crackedwords = []

with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    for word in words:
        set_word = set(word)
        if set_word.issubset(ws) and w7 in word:
            crackedwords.append(word)

for word in crackedwords:
    if len(word) < 4:
        crackedwords.remove(word)

print(crackedwords)



# PyAutoGUI

input("Press enter to start")
time.sleep(2)

for word in crackedwords:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.5)