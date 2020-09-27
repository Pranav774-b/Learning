# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:14:22 2019

@author: PranavM
"""

import matplotlib
x = [2, 4, 6]
y = [1, 3, 5]
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

primes = [2, 3, 4, 5, 6, 7]
for prime in primes:
    print(prime)
    print(primes)
    
# Prints out the numbers 0,1,2,3,4
for x in range(4):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
    
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
                print(x)

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
    
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for x in numbers:
    if x==237:
        break 
    if x%2 ==0:
            print(x)
            
            
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

def my_function():
    print("Hello From My Function!")
    
my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args("Nolan", "Byebye")

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

build_sentence("xyz")
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

