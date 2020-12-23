import pyautogui
import random
import time


message = "windows sucks"
repeats = 100
delay = 100

isLoaded = input("Input number and press ENTER.")
print("Five seconds to refocus the text input area...")

time.sleep(5)

for i in range(0,repeats):         #Message sending loop
        if message != "":
                pyautogui.typewrite(message)     
                pyautogui.press("enter")
                time.sleep(200/1000)
                pyautogui.click(button='right', x=400, y=925)
                pyautogui.keyDown('shift')
                pyautogui.click(x=500, y=1000)
                pyautogui.keyUp('shift')
                pyautogui.click()
        else:
                pyautogui.hotkey('ctrl', 'v')      
                pyautogui.press("enter")
                time.sleep(200/1000)
                pyautogui.click(button='right', x=400, y=925)
                pyautogui.keyDown('shift')
                pyautogui.click(x=500, y=1000)
                pyautogui.keyUp('shift')
                pyautogui.click()

        time.sleep(delay/1000)
print("Done\n")
