import webbrowser
import pyautogui
import time

for i in range (5):
 
 webbrowser.open("https://projected.kesug.com/")
 time.sleep(10)
 x=600
 y=600
 pyautogui.moveTo(x,y,duration=15)
 pyautogui.scroll(-2000)
 x=1870
 y=12
 pyautogui.moveTo(x,y,duration=15)
 pyautogui.click()

 webbrowser.open("http://firsttelling.com")
 time.sleep(10)
 x=600
 y=600
 pyautogui.moveTo(x,y,duration=15)
 pyautogui.scroll(-3000)
 x=1870
 y=12
 pyautogui.moveTo(x,y,duration=25)
 pyautogui.click()


