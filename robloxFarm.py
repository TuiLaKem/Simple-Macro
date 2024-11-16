import pyautogui
from time import sleep
import keyboard

# while True:
# pyautogui.moveTo(2037,1953,2,tween=pyautogui.easeInOutQuad)
# pyautogui.click()


# pyautogui.moveTo(1146   ,1006,2,tween=pyautogui.easeInOutQuad)

# pyautogui.press('1')

keyboard.press_and_release('alt+tab')

while True:
    pyautogui.click(611   ,1294)
    sleep(0.3)
    keyboard.press_and_release('1')
    sleep(0.5)
    pyautogui.click()
    keyboard.press_and_release('F')
    keyboard.press_and_release('F')
    keyboard.press_and_release('F')
    sleep(5)
    



