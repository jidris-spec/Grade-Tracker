Grade Management System

This Python script is a simple Grade Management System that allows users to add courses and their scores, display grades, and calculate the total grade. The script runs in a loop, providing a menu for user interaction until the user chooses to exit.

Features

Add Courses**: Input the course name and score to add or update the grade.
Display Grades**: Show all the courses and their corresponding scores.
Calculate Total Grade**: Compute and display the total score across all courses.

How to Use

1. Add a Course and Score**:
   - Select option `1` from the menu.
   - Enter the course name when prompted.
   - Enter the score for the course.
   - The script will add the score to the existing score if the course already exists.

2. Display Grades**:
   - Select option `2` from the menu.
   - The script will display all the courses and their scores.

3. Calculate Total Grade**:
   - Select option `3` from the menu.
   - The script will calculate and display the total score of all courses.

4. Exit the Program**:
   - Select option `4` from the menu.
   - The script will exit the loop and terminate the program.

Script Details

nitialization

python
# Initializing the Grade dictionary
grade = {}
