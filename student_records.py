# Part 4: File Handling Laboratory
# Task 4.1: Student Records File System
import pickle

students = {
    1: {"name": "Alice", "grade": "A", "major": "CS"},
    2: {"name": "Bob", "grade": "B", "major": "IT"},
    3: {"name": "Charlie", "grade": "A-", "major": "SE"}
}

def save_records(filename):
    with open(filename, 'wb') as f:
        pickle.dump(students, f)
    print("Records saved to", filename)

def load_records(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    print("Loaded Records:", data)

def export_to_text(filename):
    with open(filename, 'w') as f:
        for sid, info in students.items():
            f.write(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade']}, Major: {info['major']}\n")
    print("Exported to", filename)

# Test
save_records("students.pkl")
load_records("students.pkl")
export_to_text("students.txt")


# Task 4.2: File Operations Practice

filename = "sample.txt"

# Write mode
with open(filename, 'w') as f:
    f.write("This is a new file.\n")

# Append mode
with open(filename, 'a') as f:
    f.write("Appending a new line.\n")

# Read mode
try:
    with open(filename, 'r') as f:
        content = f.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("Error: File not found.")
