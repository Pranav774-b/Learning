# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:12:42 2020

@author: PranavM
"""
import os

names=['Jeff','Gary','Jill','Samantha']

for name in names:
    print("Hello there, "+ name) #incorrect way to write code in python although it will give you result
    print(''.join(['Hello there,', name])) #Join takes a list as argument and joins it 

print(','.join(names)) #This joins the names with a comma in the seperator

location_of_file= 'C:\\Users\\PranavM'
filename='biden.txt'

print(location_of_file+'\\'+filename)

with open(os.path.join(location_of_file,filename)) as f:
    print(f.read())
    
    
''' 
Join is important when you have to concat more than 2 string variables
similarly when you do Os.join you do not need to put \\ 
'''



who = 'Gary'
how_many='12'

print(who, 'bought', how_many, 'apples') #This gives correct result but not the right way to write code in python

print('{} bought {} apples'.format(who,how_many)) #This is the correct way
