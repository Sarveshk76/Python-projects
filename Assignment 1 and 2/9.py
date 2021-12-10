str = 'This is a string'
str1= ''
for i in range(len(str)):
    if i%2 == 0:
        str1 = str1 + str[i]
print("Original string: ",str)
print("Characters at even index: ",str1)