def Average(lst):
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    return sum/len(lst)

lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

print("Average of the list =", round(average, 2))