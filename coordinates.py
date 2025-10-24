#  Part 2: Tuples & Sets Laboratory
# Task 2.1: Coordinate System with Tuples
import math

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

# Define points
A = (2, 3)
B = (5, 7)
C = (1, 9)

points = (A, B, C)
print("Points:", points)

# Test functions
print("Distance A-B:", round(distance(A, B), 2))
print("Midpoint A-B:", midpoint(A, B))

# Demonstrate immutability
try:
    A[0] = 10
except TypeError:
    print("Error: Tuples are immutable!")

# Task 2.2: Unique Word Counter with Sets
from collections import Counter

text = "Python is a programming language. Python is easy to learn. Python is powerful."

# Split and clean words
words = text.lower().replace('.', '').split()
unique_words = set(words)

print("Words:", words)
print("Unique Words:", unique_words)
print("Total Words:", len(words))
print("Unique Word Count:", len(unique_words))

# Most common words
word_counts = Counter(words)
print("Word Frequencies:", word_counts)
print("Most Common Word:", word_counts.most_common(1)[0])
