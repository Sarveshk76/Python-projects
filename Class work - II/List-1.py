List = ['Apple','Mango','Orange','Kiwi','Banana']
List1 = []
print("List: ",List)
print("List1: ",List1)
List1.extend(List)
print("After List1.extend(List), List1: ",List1)
slice = List[0:2]
print("After List[0:2](Slice): ",slice)
List[1] = 'Lichee'
print("After Updating list: ",List)
del List[2]
print("After del List[2]: ",List)

print("After all(List): ",all(List))
print("after any(List): ",any(List))
List.sort()
print("After List.sort(): ",List)
List.pop()
print("After List.pop(): ",List)
List.remove('Kiwi')
print("After List.remove('Kiwi'): ",List)