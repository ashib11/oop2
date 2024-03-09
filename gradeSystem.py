num = int(input("Enter the number of Students: "))
marks = []

for i in range(1, num + 1):
    mark = int(input(f"Enter the obtain marks of Student-{i}: "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        break
    marks.append(mark)

avg = sum(marks) / len(marks)
avg = format(avg, ".2f")

grades = {'A+': 0, 'A': 0, 'A-': 0, 'B+': 0, 'B': 0, 'B-': 0, 'C+': 0, 'C': 0, 'D': 0, 'F': 0}

for mark in marks:
    if mark >= 80:
        grades['A+'] += 1
    elif mark >= 75:
        grades['A'] += 1
    elif mark >= 70:
        grades['A-'] += 1
    elif mark >= 65:
        grades['B+'] += 1
    elif mark >= 60:
        grades['B'] += 1
    elif mark >= 55:
        grades['B-'] += 1
    elif mark >= 50:
        grades['C+'] += 1
    elif mark >= 45:
        grades['C'] += 1
    elif mark >= 40:
        grades['D'] += 1
    else:
        grades['F'] += 1

print(f"Average Class Marks: {avg}")
print(f"Average Grade: ")
if mark >= 80:
    print("A+")
elif mark >= 75:
    print("A")
elif mark >= 70:
    print("A-")
elif mark >= 65:
    print("B+")
elif mark >= 60:
    print("B")
elif mark >= 55:
    print("B-")
elif mark >= 50:
    print("C+")
elif mark >= 45:
    print("C")
elif mark >= 40:
    print("D")
else:
    print("F")
total_students = len(marks)
grade_counts = list(grades.values())


print("Grade Distribution:")
for grade, count in grades.items():
    if count > 0:
        print(f"{grade}: {count}")
