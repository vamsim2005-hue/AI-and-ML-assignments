# Student Marks Analysis

# Create a list of student marks
marks = [78, 35, 92, 40, 61]

# Convert list into tuple
marks_tuple = tuple(marks)

# Display list and tuple
print("Student Marks List:", marks)
print("Type of List:", type(marks))

print("Student Marks Tuple:", marks_tuple)
print("Type of Tuple:", type(marks_tuple))

# Find highest and lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Count students who scored at least 40
count = marks.count(40) + (marks[0] >= 40) + (marks[1] >= 40) - (marks[0] == 40) - (marks[1] == 40)
# Alternative direct counting without loops:
count = (marks[0] >= 40) + (marks[1] >= 40) + (marks[2] >= 40) + (marks[3] >= 40) + (marks[4] >= 40)

print("Students scoring at least 40:", count)

# Check whether all marks are between 0 and 100
valid = (min(marks) >= 0) and (max(marks) <= 100)

print("Are all marks valid?", valid)

# Modify list element
marks[0] = 85
print("Modified List:", marks)

# Modify tuple element
# Tuples are immutable, so their elements cannot be changed.
try:
    marks_tuple[0] = 85
except TypeError:
    print("Tuple cannot be modified because tuples are immutable.")