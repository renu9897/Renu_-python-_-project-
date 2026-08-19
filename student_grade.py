# student_grade.py
name = input("Enter student name: ")
marks = float(input("Enter marks out of 100: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print(f"\nStudent: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")