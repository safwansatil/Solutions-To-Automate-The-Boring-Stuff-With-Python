# This is a simple program that greets the user and asks for their name and age.

print('Hello World!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' +str(int(myAge) +1) + ' in a year then huh.')