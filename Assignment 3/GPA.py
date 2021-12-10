def gp(grade):
    if grade == 'a':
        return  4.0
    if grade == 'b':
        return 3.0
    if grade == 'c':
        return 2.0
    if grade == 'd':
        return 1.0
    if grade == 'f':
        return 0.0
History = gp('a')
Math = gp('b')
English = gp('c')
print("History=",History,",","Math=",Math,",","English=",English)
print("GPA: ",History+Math+English/3)