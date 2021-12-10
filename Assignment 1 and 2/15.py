s_name = input('Enter name of Student : ')
s_roll = int(input('Enter Roll no of Student : '))
s_div = input("Enter Div of student :")
sport_marks = int(input('Enter marks of Student for Sports Event out of 20: '))
activity1_marks = int(input('Enter marks of Student for Activity 1 out of 10: '))
if sport_marks > 20 or sport_marks < 0:
    print('Enter marks in range 0 - 20')
    sport_marks = int(input('Enter marks of Student for Sports Event out of 20:'))
    activity1_marks = int(input('Enter marks of Student for Activity 1 out of 10: '))
if activity1_marks > 10 or activity1_marks < 0:
    print('Enter marks in range 0 - 10')
    activity1_marks = int(input('Enter marks of Student for Activity 1 out of 10:'))
    activity2_marks = int(input('Enter marks of Student for Activity 2 out of 10: '))
if activity2_marks > 10 or activity2_marks < 0:
    print('Enter marks in range 0 - 10')
    activity2_marks = int(input('Enter marks of Student for Activity 2 out of 10:'))
    activity3_marks = int(input('Enter marks of Student for Activity 3 out of 10: '))
if activity3_marks > 10 or activity3_marks < 0:
    print('Enter marks in range 0 - 10')
    activity3_marks = int(input('Enter marks of Student for Activity 3 out of 10:'))
    examination_marks = int(input('Enter marks of Student for Examination out of 50:'))
if examination_marks > 50 or examination_marks < 0:
    print('Enter marks in range 0 - 50')
    examination_marks = int(input('Enter marks of Student for Examination out of50: \n'))
result = sport_marks + activity1_marks + activity2_marks + activity3_marks +examination_marks
print('STUDENT RESULT'.center(60, '*'))
print('STUDENT NAME\tSTUDENT ROLL\tSTUDENT DIV\t\tACTIVITY NAME\tMARKS OBTAINED')
print('{}\t\t{}\t\t\t\t{}\t\t\tSPORTS\t\t\t\t\t{}'.format(s_name,
s_roll,s_div, sport_marks))
print('\t\t\t\t\t\t\t\t\t\t\t\tACTIVITY 1\t\t\t\t{}'.format(activity1_marks))
print('\t\t\t\t\t\t\t\t\t\t\t\tACTIVITY 2\t\t\t\t{}'.format(activity2_marks))
print('\t\t\t\t\t\t\t\t\t\t\t\tACTIVITY 3\t\t\t\t{}'.format(activity3_marks))
print('\t\t\t\t\t\t\t\t\t\t\t\tEXAMINATION\t\t\t\t{}'.format(examination_marks
))
print('-' * 80)
print('\t\t\t\t\t\t\t\t\t\t\t',s_name,'RESULT\t\t=\t', result, '%')