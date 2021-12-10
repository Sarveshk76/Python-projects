def nearest_palindrom(num):
    temp = num
    rev = 0
    while temp > 0:
        numDig = temp % 10
        rev = rev * 10 + numDig
        temp = temp // 10
    print("The reverse of num is:", rev)
    if rev == num:
        print("The given number is Palindrome.")
    else:
        print("The given number is not Palindrome.")

nearest_palindrom(1222)
nearest_palindrom(1221)