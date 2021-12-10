str = input('Enter a string: ')
digit = 0
letter = 0
for i in str:
    if i.isdigit():
        digit += 1
    else:
       letter += 1
print("Digits :",digit)
print("Letters: ",letter)