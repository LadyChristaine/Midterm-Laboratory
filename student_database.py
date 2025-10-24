#  Part 3: Dictionaries Laboratory
# Task 3.1: Student Database

students = {}

def add_student(student_id, name, grade, major):
    students[student_id] = {'name': name, 'grade': grade, 'major': major}
    print(f"Added {name} (ID: {student_id})")

def get_student(student_id):
    return students.get(student_id, "Student not found.")

def update_grade(student_id, new_grade):
    if student_id in students:
        students[student_id]['grade'] = new_grade
        print(f"Updated grade for {students[student_id]['name']} to {new_grade}")
    else:
        print("Student not found.")

def display_all():
    print("\nAll Students:")
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade']}, Major: {info['major']}")

# Test data
add_student(101, "Alice", "A", "Computer Science")
add_student(102, "Bob", "B+", "Information Tech")
add_student(103, "Charlie", "A-", "Software Eng")

update_grade(102, "A")
display_all()

# Task 3.2: Word Frequency Counter
text = "Data science is fun. Science uses data to find patterns. Data and science are powerful together."

words = text.lower().replace('.', '').split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

print("Word Frequencies:")
for word, freq in sorted_words:
    print(f"{word}: {freq}")

most_common = sorted_words[0]
print("\nMost Common Word:", most_common)
