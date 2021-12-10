file1=open("file.txt", "w")
file1.write("Students are expected\t to undertake\t one mini project starting\n from first semester\n till third semester\n")
file1.close()
with open("file.txt") as file:
    text=file.read()
    print(text)
    tab,space,newline=0,0,0
    for char in text:
        if char=='\t':
            tab+=1
        if char==' ':
            space+=1
        if char=='\n':
            newline+=1
print("No.of tabs: ", tab)
print("No. of spaces: ", space)
print("No. of newline:  ", newline)