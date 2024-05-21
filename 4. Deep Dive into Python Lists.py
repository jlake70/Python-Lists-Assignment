# Task 1

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

students_below  = students[2:3]
grades_below = grades[2:3]
activities_below = activities[2:3]



#failing = "".join(students_below, grades_below, activities_below)
print(students_below, grades_below, activities_below)

# Task 2 and #Task 3
students.pop(2)
students_approved = list()
students_approved.append(students)


print("students_approved = ",students_approved)
print(students_approved)