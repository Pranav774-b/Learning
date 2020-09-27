# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:56:42 2019

@author: PranavM
"""
import pyautogui
width, height=pyautogui.size()

"Controlling the Mouse"
pyautogui.position()
pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10,duration=5)
pyautogui.moveRel(500, 0) #moves the mouse relative to the current position 


pyautogui.displayMousePosition() # to check the position of the mouse at the moment. However, it is better to use it in CMD

"Controlling the Keeyboard"
pyautogui.click()
pyautogui.typewrite(('Hello World'))






from tkinter import *

root = Tk()

topframe = frame(root)
topframe.pack()

bottomframe = frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topFrame,text = 'Button1')


root.mainloop()