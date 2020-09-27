# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:23:54 2019

@author: PranavM
"""


import json

data=json.load(open(r'C:\Users\PranavM\OneDrive\Python/data.json'))

import difflib
from difflib import SequenceMatcher

from difflib import get_close_matches

#function to return the definition of a word from the dict data type
def translate(w):
    w= w.lower() #to lowercase all data since that is what we have 
    if w in data: #to check if the word input is in the dictionary 
        return data[w]
    elif input('did you mean %s? Enter Capital Y or N only: '  %get_close_matches(w,data.keys(),n=1)) == 'Y':
        return data[get_close_matches(w,data.keys())[0]]
    else:
        return('The word does not exist. Please check it')

#get_close_matches(word,data.keys(),n=1) passes the output as a dict type and not string. 
#While get_close_matches(w,data.keys())[0] passes as a string

word = input("Enter Word:")
output= translate(word)
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)




#else:
    
    print ('did you mean %s?'  %get_close_matches(word,data.keys(),n=1))
    
    
    print ("Word not found")



## these are test codes. This is to check which functions to use in my application.
print(word.lower())

#checks if the word in the dict 
"rain" in data

#for getting a matching set of string 
#import difflib
#from difflib import SequenceMatcher

#this function gives you the matching ratio between two words entered
#SequenceMatcher(None, "rainn", "rain").ratio()

#get_close_matches gives close matches of the word in a given dict 
#from difflib import get_close_matches

#help(get_close_matches)

#get_close_matches('rainn', data.keys(), n=1)
