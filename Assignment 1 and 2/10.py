#10. Write the program to remove the duplicates from the list.

List = [1,2,2,2,3,3,4,4,5,55,5]
NewList = []
for i in List:
    if i not in NewList:
        NewList.append(i)
print("List: ",List)
print("After removing duplicates: ",NewList)
