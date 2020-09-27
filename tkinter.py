# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:29:44 2020

@author: PranavM
"""

from tkinter import *
from PIL import Image, ImageTk



#the Class window is just a frame initialiser 
class Window(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master=None)
        
        self.master=master #defining the master widget 
        self.init_window()
    
    def init_window(self): #here we are initialising the window
        self.master.title("GUI") #the title of the window is GUI
        self.pack(fill=BOTH, expand =1)
        
        '''
        # quitButton=Button(self, text='QUIT', command=self.client_exit)
        
        # quitButton.place(x=0, y=0)
        '''
        
        
        ''' The below two lines define that we have a menu and where it goes'''
        menu_file= Menu(self.master) #this is saying that this is menu in the main window 
        self.master.config(menu=menu_file) #we are defining the instance of the menu
        
        ''' The below three are created for a file button and adding an exit to it.'''
        file = Menu(menu_file)
        file.add_command(label='Save', command =self.client_exit)
        file.add_command(label='Exit', command =self.client_exit)
        menu_file.add_cascade(label='File', menu = file)
        
        edit = Menu(menu_file)
        edit.add_command(label='Show Image', command= self.showImg)
        edit.add_command(label='Show Text', command= self.showTxt)
        menu_file.add_cascade(label='Edit', menu=edit)
        
    def showImg(self):
        load=Image.open(r'C:\Users\PranavM\Pictures\meme.jpg')
        render=ImageTk.PhotoImage(load)
        
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)
    
    def showTxt(self):
        text=Label(self, text= 'hey there good looking')
        text.pack()
    
    def client_exit(self):
        root.destroy() #want to destroy root which is what the window is. Self.destroy with destroy the button




        
root =Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
        
        