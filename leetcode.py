def findMed(num1:list[int],num2:list[int]):
    for i in range(len(num2)):
        num1.append(num2[i])
    print(num1)
    print(len(num1)+1/2)
num1 = [1,3]
num2 = [2,4]
findMed(num1,num2)
