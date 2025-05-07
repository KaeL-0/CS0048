import os

def pause():
    print()
    input('Enter to continue')
    os.system('cls' if os.name =='nt' else 'clear')

def main():

    os.system('cls' if os.name =='nt' else 'clear')

    while True:

        print('-- Welcome to Temperature Converter ---')
        print()
        print('Menu:')
        print()
        print('1. Convert Celsius to Fahrenheit')
        print('2. Convert Fahrenheit to Celsius')
        print('3. Exit')
        print()

        choice = input('Enter your choice here: ')

        if choice == '1':
            celsius = int(input('Enter temperature in Celsius: '))
            fahrenheit = (celsius * 9/5) + 32
            print()
            print(f'Temperature in Fahrenheit: {fahrenheit}')
            pause()
        elif choice == '2':
            fahrenheit = int(input('Enter temperature in Fahrenheit: '))
            celsius = (fahrenheit - 32) * 5/9
            print()
            print(f'Temperature in Celsius: {celsius}')
            pause()
        elif choice == '3':
            print()
            print('Exiting Temperature Converter...')
            print()
            input('Press any key to exit')
            print()
            break
        else:
            print('Invalid input, please try again...')
            pause()

if __name__ == "__main__":
    main()