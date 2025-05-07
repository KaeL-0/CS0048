import os
import random

def pause():
    print()
    input('Enter to continue')
    os.system('cls' if os.name =='nt' else 'clear')

def guessingGame():
        randomNum = random.randrange(1, 101)
        attempt = 0

        while True:
            print()
            guessNum = int(input('Guess the number (1-100): '))

            if guessNum > randomNum:
                print()
                print('Too high')
                attempt += 1
            elif guessNum < randomNum:
                print()
                print('Too low')
                attempt += 1
            else:
                print()
                attempt += 1
                print(f'Congratulations! You guessed the number in {attempt} attempts.')
                pause()
                break

def main():

    os.system('cls' if os.name =='nt' else 'clear')

    while True:

        print('-- Welcome to Number Guessing Game ---')
        print()
        print('Menu:')
        print()
        print('1. Play Number Guessing Game')
        print('2. Exit')
        print()

        choice = input('Enter your choice here: ')

        if choice == '1':
            guessingGame()

        elif choice =='2':
            print()
            print('Exiting Number Guessing Game...')
            print()
            input('Press any key to exit')
            print()
            break
        else:
            print('Invalid input, please try again...')
            pause()

if __name__ == "__main__":
    main()