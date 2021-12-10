jack = {"name": "Jack Frost",
        "examination": [90, 80, 85, 95],
        "sports": [85, 85],
        "activities": [88.20, 87.20]
        }

james = {"name": "James Potter",
         "examination": [92, 86, 84, 90],
         "sports": [80, 90],
         "activities": [87.90, 98.72]
         }

dylan = {"name": "Dylan Rhodes",
         "examination": [87, 82, 93, 89],
         "sports": [88, 97],
         "activities": [80, 80]
         }

jess = {"name": "Jessica Stone",
        "examination": [87, 75, 77, 91],
        "sports": [90, 80],
        "activities": [89, 84.56]
        }

tom = {"name": "Tom Hanks",
       "examination": [79, 89, 60, 86],
       "sports": [85, 76],
       "activities": [80, 70.6]
       }


def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


def calculate_total_average(students):
    examination = get_average(students["examination"])
    sports = get_average(students["sports"])
    activities = get_average(students["activities"])


    return (0.5 * examination +
            0.2 * sports + 0.3 * activities)


def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


def class_average_is(student_list):
    result_list = []

    for student in student_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
        return get_average(result_list)

students = [jack, james, dylan, jess, tom]

for i in students:
    print(i["name"])
    print("-----------------------------------")
    print("Average marks of %s is : %s " % (i["name"],
                                            calculate_total_average(i)))

    print("Grade of %s is : %s" % (i["name"],
                                          assign_letter_grade(calculate_total_average(i))))

    print()

class_av = class_average_is(students)

print("Class Average is %s" % (class_av))
print("Letter Grade of the class is %s "
      % (assign_letter_grade(class_av)))