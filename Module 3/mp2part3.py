import os

def pause():
    print()
    input('Enter to continue')
    os.system('cls' if os.name =='nt' else 'clear')

os.system('cls' if os.name =='nt' else 'clear')

taskArr = []

while True:

    print('-- To-Do List ---')
    print()
    print('Menu:')
    print()
    print('1. Add Task')
    print('2. Remove Task')
    print('3. View Tasks')
    print('4. Exit')
    print()

    choice = input('Enter your choice here: ')

    if choice == '1':
        print()
        task = input('Enter the task to add: ')
        taskArr.append(task)
        pause()
    elif choice == '2':
        print()
        task = input('Enter the task to remove: ')
        taskArr.remove(task)
        pause()
    elif choice == '3':
        print()
        print('Task to-do list: ')
        for tasks in taskArr:
            print(tasks)
        pause()
    elif choice == '4':
        print()
        print('Thank you for using my program...')
        print()
        input('Press any key to exit')
        print()
        break
    else:
        print('Invalid input, please try again...')
        pause()
