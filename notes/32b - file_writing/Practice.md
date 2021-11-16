# File I/O Practice
## Part 1 - Text Files
For the first part of this exercise assume you have a file called `students.txt` which simply contains a bunch of student names, one name per line. Your goal is to write two functions:
* `addStudent` - accepts a parameter of `firstName` and `lastName` and writes to a file called `students.txt`.
* `findStudent` - accepts a parameter of `firstName` and returns the first student found

### Challenges
Write the following additional functions:
* `updateStudent` - accepts a parameter of `firstName` and `newName` and updates first student found
* `removeStudent` - accepts a parameter of `firstName` and removes the student from the text file
Add a unique id for each student so that you can find a student by their id instead of first name (which breaks if you have the same first name for multiple students)

## Part 2 - CSV (Comma Separated Values)
For the next part of this exercise, you will be working with CSVs, so first create a file called `users.csv` and then work on the following two functions:

one that prints out all of the first and last names in the `users.csv` file
one that prompts us to enter a first and last name and adds it to the `users.csv` file.

The above exercises were preserved from: https://www.rithmschool.com/courses/python-fundamentals-part-2/python-file-io-exercise on Nov 16, 2021.
