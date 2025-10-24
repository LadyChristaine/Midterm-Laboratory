#  Part 1: Lists Laboratory
# Task 1.1: Student Grade Manager

# Lists to store student names and grades
students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}")

def display_students():
    print("\nStudent Grades:")
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")

def average_grade():
    return sum(grades) / len(grades)

def highest_grade():
    return max(grades)

# Test the functions
add_student("Alice", 85)
add_student("Bob", 92)
add_student("Charlie", 78)

display_students()
print(f"\nAverage Grade: {average_grade():.1f}")
print(f"Highest Grade: {highest_grade()}")

# Task 1.2: List Operations Practice

numbers = [5, 2, 8, 1, 9, 3]

print("Original List:", numbers)

numbers.sort()
print("Sorted List:", numbers)
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("List Length:", len(numbers))
