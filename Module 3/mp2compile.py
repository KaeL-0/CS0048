import os
import mp2part1
import mp2part2
import mp2part3
import mp2part4
import mp2part5

def pause():
    print()
    input('Enter to continue')
    os.system('cls' if os.name =='nt' else 'clear')
      

def main():
    
    os.system('cls' if os.name =='nt' else 'clear')

    while True:

        print('--- MP2 System Compilation ---')
        print()
        print('Menu:')
        print()
        print('1. Simple Calculator')
        print('2. Temperature Converter')
        print('3. To-Do List')
        print('4. Number Guessing Game')
        print('5. Student Grade Calculator')
        print('6. Exit')
        print()

        choice = input('Enter your choice here: ')
        print()

        if choice == '1':
            mp2part1.main()
        elif choice == '2':
                mp2part2.main()
        elif choice == '3':
                mp2part3.main()
        elif choice == '4':
                mp2part4.main()
        elif choice == '5':
                mp2part5.main()
        elif choice == '6':
                print()
                print('Thank you for using my programs...')
                print()
                input('Press any key to exit')
                print()
                break
        else:
            print('Invalid input, please try again...')
            print('Please enter a number 1-6')
            pause()

if __name__ == '__main__':
      main()