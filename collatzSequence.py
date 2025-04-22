def collatz(number):
    if(number%2 ==0):
        return number //2
    if(number%2 !=0):
        num = 3*number +1
        return num
    
def main():
    print('Enter a number: ')
    try:
        num = int(input())
        while num != 1:
            print(num)
            num = collatz(num)  
        print(num)  
    except ValueError:
        print('Please enter a valid number.')
        
main()