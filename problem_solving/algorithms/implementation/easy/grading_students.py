#!/bin/python3
def gradingStudents(grades):
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        else:
            for x in range(0, 5):
                if (x + i) % 5 == 0:
                    if x+i - i < 3:
                        new_grades.append(x + i)
                    else:
                        new_grades.append(i)

    return new_grades