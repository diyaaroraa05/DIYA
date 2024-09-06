# Input student details
roll_no = input("Enter Roll No.: ")
name = input("Enter Name: ")
student_class = input("Enter Class: ")

# Input marks for each subject
english = int(input("Enter marks for English: "))
maths = int(input("Enter marks for Maths: "))
science = int(input("Enter marks for Science: "))
social_science = int(input("Enter marks for Social Science: "))
computer = int(input("Enter marks for Computer: "))

# Calculate total and percentage
total_marks = english + maths + science + social_science + computer
percentage = (total_marks / 500) * 100

# Determine grade
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 50:
    grade = 'E'
else:
    grade = 'F'

# Print result in tabular form
print("\n--- Student Result ---")
print(f"{'Roll No.'} : {roll_no}")
print(f"{'Name'} : {name}")
print(f"{'Class'} : {student_class}")

print(f"{'Subject':<20}{'Marks Obtained':>15}")
print("-" * 35)
print(f"{'English':<20}{english:>15}/100")
print(f"{'Maths':<20}{maths:>15}/100")
print(f"{'Science':<20}{science:>15}/100")
print(f"{'Social Science':<20}{social_science:>15}/100")
print(f"{'Computer':<20}{computer:>15}/100")
print("-" * 35)
print(f"{'Total Marks':<20}{total_marks:>15}/500")
print(f"{'Percentage':<20}{percentage:>14.2f}%")
print(f"{'Grade':<20}{grade:>15}")
