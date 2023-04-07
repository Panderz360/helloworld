'''Caculator/will add, subtract, multiply and divide'''
# what we need to do: 1. take input, 2. manipulate input, 3. give a proper **correct** output

# data manipulation functions
def add(num1,num2):
    '''THis function adds two numbers'''
    return  num1+num2

def subtract(num1,num2):
    '''This function subtracts two numbers'''
    return  num1-num2

def multiply(num1,num2):
    '''This function multiply two numbers'''
    return  num1*num2

def divide(num1,num2):
    '''This function divide two numbers'''
    return  num1/num2

def calculate():

    num1 = int(input("Please input a number:"))

    num2 = int(input("Please input a number:"))

    choice = input("\nWhat type of operation do you want?\n+\n-\n*\n/\n")

    if choice == '+':
        print(f"Adding both numbers equal: {add(num1,num2)}")
    elif choice == '-':
        print(f"Subtracting both numbers equal: {subtract(num1,num2)}")
    elif choice == '*':
         print(f"Multiplying both numbers equal: {multiply(num1,num2)}")
    elif choice == '/':
        print(f"dividing both numbers equal: {divide(num1,num2)}")
    else:
        print("Please choice the right operator next time!\n")