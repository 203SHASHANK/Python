# Function to input student information
def input_student_info():
    print("Enter student information:")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = float(input("Grade: "))
    return name, age, grade

# Function to display student information
def display_student_info(student):
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Grade:", student['grade'])

# Function to find average grade of all students
def average_grade(students):
    total = sum(student['grade'] for student in students)
    return total / len(students)

# Main function
def main():
    students = []  # List to store student dictionaries
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Average Grade")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_info = input_student_info()
            student_dict = {'name': student_info[0], 'age': student_info[1], 'grade': student_info[2]}
            students.append(student_dict)
            print("Student added successfully!")
        elif choice == 2:
            print("\nAll Students:")
            for student in students:
                display_student_info(student)
        elif choice == 3:
            if not students:
                print("No students added yet.")
            else:
                print("Average Grade:", average_grade(students))
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()