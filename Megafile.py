# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:19:46 2019

@author: PranavM
"""
#28/08/19
import datetime 
datetime.datetime.now()

monday_temperatures= [9.1, 8.8, 7.5]
monday_temperatures.pop()
monday_temperatures.__getitem__(1)

def password_controller(string):
    if len(string)<8:
        return "False"
    else:
        return "True"

password_controller('Mayekar')

#using for loop to get round numbers from a given list 
monday_temperatures= [9.1, 8.8, 7.5]
for temperature in monday_temperatures:
    print(round(temperature))

for letter in "Hello":
    print (letter) 
print ("done")
    
colors = [11, 34, 98, 43, 45, 54, 54]

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))
    
dir(dict.items)
    