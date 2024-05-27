#  initializing the Grade
grade = {}

# function to add courses
def add_courses():
    course_name = input("Enter your course name:")
    score = float(input("ENTER YOUR SCORE:"))
    if course_name in grade:
        grade[course_name] += score
    else:
        grade[course_name] = score
    print (f"You scored {score} in {course_name}.")

# To display grade

def display_grade():
    print("here are your grades")
    for course_name, score in grade.items():
        print(f"Your overall score in {course_name} is {score} keep up the good job.")

# To calculate total grade
def calculate_total_grade():
    total = sum(grade.values())
    print(f"total score: {total}")
calculate_total_grade()

# looping of functions
while True:
    print("\n1.Add course_name\n2. Display grade\n3. Calculate_total_grade\n4. Exit")
    choice=input("Choose course_name:")

    if choice == "1":
        add_courses()
    elif choice == "2":
        display_grade()
    elif choice == "3":
        calculate_total_grade()
    elif choice == "4":
        print("so sad to see you leave.")
        break
    else:
        print("invalid choice try again later.")






    