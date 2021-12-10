myDict ={1:'Apple',2:'Orange',3:'Kiwi'}
print("myDict: ",myDict)
myDict1 = myDict.copy()
print("After myDict.copy() myDict1: ",myDict1)
print("After myDict.fromkeys({4,5,6},'Mango'): ",myDict.fromkeys({4,5,6},'Mango'))
print("After myDict.get(2): ",myDict.get(2))
print("After myDict.items(): ",myDict.items())
print("After myDict.setdefault(2,'Cherry'): ",myDict.setdefault(2,'Cherry'))