for j in range(1,31):
    if j % 3==0 and j % 5==0:
        print("Fizz Buzz..")
    elif j % 5 == 0:
        print("Buzz..")
    elif j % 3==0:
         print("Fizz..")
    else:
        print(j)
