# UA-High-Grade-Book

This program was part of a Udemy.com final project.
It is a Student Grade Book.
To make this fun for me I kind of catered this around UA High which is from an Anime Series My Hero Academia.

When you first launch the program it is going to ask you for a Username and Password.
The username and passwords are contained in a Dictionary file named admins
If the username is invalid it will print Invalid username, heroes will be dispached to this location.
If the password is invalid it will print Invalid password, no villains allowed.

Once in the program you have the abilty to do the following:
View Students - This will show a list of the students and their grades
Add Grades - Allows you to add grades to a specific student
Remove Grades - Allows you to remove a grade from a student
Add Student - Allows you to add in a new student with a grade
Remove Student - Allows you to remove a student
Students Average Grade - gives you the average of all the grades for each student
Exit - exit the program

View Students is pretty self explanitory.
- I created a dictionary called: studentDict and added a bunch of students from UA High + their grades.
- View Students just prints the dictionary.
Add Grades
- calls the function studGrades - asks for student name and asks for the grade that needs to be added.
- it will go through the studentDict and look for studName that was added and it will append the studentDict with the studGrade that was inputted from the user.
- else - if the student name does not exist it will print Student does not exist.
Remove Grades 
- this calls the function delStudGrade - this does the same thing as Add grades does except it allows you to remove a grade already in the dictionary.
Add Student
- this calls the function addStud.
- this function asks you to enter a new student name and also asks you to enter the grade this student received.
- it then just adds the new student name along with the grade to the studentDict list
Remove Student
- calls the function remStud
- asks you who you want to remove then does a simple del on studentDict using the name provided by the user.
- if the name does not exist it prints Student does not exist
Students Average Grades
- calls the function avgStudGrade
- this runs a for loop - each student in studentDict.
- we define the student and grades by using the variable gradeList = studentDict[eachStudent]
- we define what we are trying to accomplish (get the average of the grades) by creating a variable avgGrade = statistic.mean(gradeList)
- this is pretty much saying calculate the average of the grades for each student from gradeList
- then we print eachStudent (which is actually each students name) and displays their average grade is avgGrade
Exit
- I imported sys and used sys.exit()
- I found out later I could have just done exit()
