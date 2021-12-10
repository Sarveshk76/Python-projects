Tuple1 = (1,2,3,4,5)
Tuple2 = ('a','b','c','d','e')
print(Tuple1)
print(Tuple2)
print("After Tuple1.index(1): ",Tuple1.index(1))

print("After Tuple1.count(1): ",Tuple1.count(1))
x = zip(Tuple1,Tuple2)
print("After zip(Tuple1,Tuple2): ",tuple(x))