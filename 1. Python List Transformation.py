# Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades_sorted = sorted(grades, reverse = True)
print(grades_sorted)

#Task 2

grades_total = sum(grades)

grades_list = len(grades)

grades_average = grades_total/grades_list
print(grades_average)

#Task 3
grades = ["Failed" if grade < 80 else grade for grade in grades]
print("Updated grades: ", grades)

#I could not figure out how to do this using the replace() function can you provide example in comments when graded