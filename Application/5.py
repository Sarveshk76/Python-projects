def find_duplicates(n):
   List = []
   for i in range(1,n+1):
      print("Enter number ",i,": ")
      num = int(input())
      List.append(num)
   print(List)
   duplicates = []
   duplicates = list(set(List).intersection())
   if duplicates == List:
      print([])
   else:
      print(duplicates)
num = int(input("Enter number of elements: "))
find_duplicates(num)