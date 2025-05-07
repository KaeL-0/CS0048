import os

def pause():
    print()
    input('Enter to continue')
    os.system('cls' if os.name =='nt' else 'clear')

def add(a, b):
    
    print(f'Result: {a+b}')
    pause()

def subtract(a, b):
    print(f'Result: {a-b}')
    pause()

def multiply(a, b):
    print(f'Result: {a*b}')
    pause()

def divide(a, b):
    print(f'Result: {a/b}')
    pause()

os.system('cls' if os.name =='nt' else 'clear')

while True:

    print('-- Welcome to Python Calculator ---')
    print()
    print('Menu:')
    print()
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    print()

    

    choice = input('Enter your operation here: ')

    if choice == '5':
        print()
        print('Thank you for using my program...')
        print()
        input('Press any key to exit')
        print()
        break

    print()
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

    if choice == '1':
        add(a, b)
    elif choice == '2':
        subtract(a, b)
    elif choice == '3':
        multiply(a, b)
    elif choice == '4':
        divide(a, b)
    else:
        print('Invalid input, please try again...')
        pause()
