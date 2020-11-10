import statistics
import sys

admins = {'Chuck': 'p@ss123$', 'Nezu': 'AnimalsRule', 'All Might': 'SM@SH!!'}

studentDict = {'Midoriya': [88, 90, 99],
               'Bakugo': [81, 85, 95],
               'Uraraka': [85, 80, 94],
               'Yaoyorozu': [100, 100, 100],
               'Mineta': [75, 79, 80],
               'Todoroki': [98, 99, 100]}


def studGrades():
    studName = input('Student Name: ')
    studGrade = input('Grade: ')

    if studName in studentDict:
        print('Adding Grade...')
        studentDict[studName].append(int(studGrade))
    else:
        print('Student does not exist!')

    print(studentDict)


def delStudGrade():
    studName = input('Student Name: ')
    studGrade = input('What Grade are we removing? ')

    if studName in studentDict:
        print('Removing Grade...')
        studentDict[studName].remove(int(studGrade))
    else:
        print('Student does not exist!')

    print(studentDict)


def addStud():
    studName = input('Who are we adding to the grade book? ')
    studGrade = input('What Grade did they get? ')
    print('Adding ', studName, 'with a grade of ', studGrade, ' to the grade book.')
    studentDict[studName] = [(int(studGrade))]

    print(studentDict)


def remStud():
    studName = input('What student would you like to remove from the grade book? ')
    if studName in studentDict:
        print('Removing ', studName, ' from the grade book..')
        del studentDict[studName]
    else:
        print('Student does not exist!')
    print(studentDict)


def avgStudGrade():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = statistics.mean(gradeList)
        print(eachStudent, 'has an average grade of:', avgGrade)


def mainWindowLoop():
    print("""\n Welcome to UA High School
    
    [1] - View Students
    [2] - Add Grades
    [3] - Remove Grades
    [4] - Add Student
    [5] - Remove Student
    [6] - Students Average Grades
    [7] - Exit Program
    """)

    action = input('What would you like to do today? (Enter a Number) ')

    if action == '1':
        print(studentDict)
    elif action == '2':
        studGrades()
    elif action == '3':
        delStudGrade()
    elif action == '4':
        addStud()
    elif action == '5':
        remStud()
    elif action == '6':
        avgStudGrade()
    elif action == '7':
        sys.exit()
    else:
        print('No valid number was chosen. Go PLUS ULTRA and try again!')


login = input('Username: ')
password = input('Password: ')

if login in admins:
    if admins[login] == password:
        print('Welcome', login, 'Go PLUS ULTRA!', '\n')
        while True:
            mainWindowLoop()
    else:
        print('Invalid Password, No Villains Allowed')
else:
    print('Invalid Username, Heroes will be dispatched to this location')
