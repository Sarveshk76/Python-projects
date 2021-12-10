string = "Welcome to Python Learning"
i = 0
print('Iterating string letters: ')
while i < len(string):
    print("Element of string: ", string[i])
    i += 1

print('Reversed string: ')
i=1
while i<=len(string):
    print(string[-i],end=" ")
    i += 1