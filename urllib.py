# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:17:08 2020

@author: PranavM
"""

'''
This code is using urllib and re to parse data from a website (doing what Beautiful Soup does)
'''

import urllib
import urllib.request
import urllib.parse
import re

# x=urllib.request.urlopen('https://www.google.com')

#print(x.read())

url='http://pythonprogramming.net'
values={'s':'basics',
        'submit':'search'}

data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()

print(respData)


paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)