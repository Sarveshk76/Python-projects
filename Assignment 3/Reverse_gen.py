def rev(str):
    length=len(str)
    for i in range(length -1,-1,-1):
        yield str[i]
name=input("Enter a String : ")
print("Reversed string : ")
print(list(rev(name)))