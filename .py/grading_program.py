'''
Translate the scores into the grades.

Scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
'''

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
    }

student_grades = {}

for stu in student_scores:
    if int(student_scores[stu]) < 71:
        student_grades[stu] = "Fail"
    elif int(student_scores[stu]) < 81:
        student_grades[stu] = "Acceptable"
    elif int(student_scores[stu]) < 91:
        student_grades[stu] = "Exceeds Expectations"
    else:
        student_grades[stu] = "Outstanding"

print(student_grades)
