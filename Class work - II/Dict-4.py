myDict = {x:x*x for x in range(1,11)}
print("myDict: ",myDict)
del myDict[2]
print("After del myDict[2]: ",myDict)
myDict.pop(8)
print("After myDict.pop(8): ",myDict)
myDict.clear()
print("After myDict.clear(): ",myDict)