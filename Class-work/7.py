name = input("Enter your name: ")
print("Enter your subject marks (out of 50)")
sub1 = int(input("Maths: "))
sub2 = int(input("Science: "))
sub3 = int(input("History: "))
sub4 = int(input("Geography: "))
total = sub1+sub2+sub3+sub4
agg = (total/200)*100
print(60*'*')
print("Name of student: ",name)
print("Aggregate(in %): ",agg)
if(agg>=75):
    print("Grade: Distinction")
elif(agg>=60 & agg<75):
    print("Grade: First division")
elif(agg>=50 & agg<60):
    print("Grade: Second division")
elif(agg>=40 & agg<50):
    print("Grade: Third division")
else:
    print("Grade: Fail")