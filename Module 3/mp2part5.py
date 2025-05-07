import os

def pause():
    print()
    input('Enter to continue')
    os.system('cls' if os.name =='nt' else 'clear')

os.system('cls' if os.name =='nt' else 'clear')

listScore = []

while True:

    print('-- Student Grade Calculator ---')
    print()
    print('Menu:')
    print()
    print("1. Add Score")
    print('2. View Score')
    print('3. Calculate Average')
    print('4. Exit')
    print()

    choice = input('Enter your choice here: ')

    if choice == '1':
        print()
        subj = input('Enter Subject Name: ')
        score = int(input('Enter Score: '))
        listScore.append({
            'Subject': subj,
            'Score': score
             })
        print()
        print("Subject's score has been added")
        pause()

    elif choice == '2':
        print()
        print('-- Student Grades -- ')
        print()
        for i in listScore:
            print(f'{i['Subject']}: {i['Score']}')
        pause()
    elif choice == '3':
        print()
        average = 0
        for i in listScore:
            average += i['Score']
        average /= len(listScore)

        print('-- Student Grade Average -- ')
        for i in listScore:
            print(f'{i['Subject']}: {i['Score']}')
        print(f'Total Average: {average}')
        pause()
    elif choice =='4':
        print()
        print('Thank you for using my program...')
        print()
        input('Press any key to exit')
        print()
        break
    else:
        print('Invalid input, please try again...')
        pause()