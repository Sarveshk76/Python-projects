num = int(input("Enter the number between 1 to 7: "))
if(num > 7 | num < 0):
    print("Enter the number between 1 to 7")
else:
    if num == 1:
        print("Its Monday")
    elif num == 2:
        print("Its Tuesday")
    elif num == 3:
        print("Its Wednesday")
    elif num == 4:
        print("Its Thursday")
    elif num == 5:
        print("Its Friday")
    elif num == 6:
        print("Its Saturday")
    elif num == 7:
        print("Its Sunday")