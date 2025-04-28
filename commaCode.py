def commaCode(items):
    output = ''
    for i in range(len(items)-1):
        output += str(items[i])
        output += ', '
    output += 'and '
    output += items[len(items)-1]
    print(output)
spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)    
#I hard coded this just for example, you can also take input, output