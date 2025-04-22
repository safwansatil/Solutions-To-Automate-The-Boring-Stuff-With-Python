# a simple python code that allows user to guess a number
import random
from sys import *

print('Heya! I am thinking of a number between 1 and 100.')
print('Wanna guess it?')
print('BTW, Type exit, if you wanna leave :( ')
target = random.randint(1, 999)

while True:
    response = input()
    if response == 'exit' or response == 'e':
        exit()
    elif target == int(response):
        print('Yayy! Good job!')
        break
    elif target < int(response):
        print('Too high!')
        print('Try again!')
    elif target > int(response):
        print('Too low!')
        print('Try again!')
    else:
        print('Please enter a valid number!')