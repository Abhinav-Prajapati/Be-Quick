
import pyautogui as gi
import time 
time.sleep(3)
with open('question.c') as f:
    line =f.readlines()
for line in line:

    gi.write(line.strip())
    gi.press("enter")
