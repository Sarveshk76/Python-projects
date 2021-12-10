list=[1] 
for i in range(5):
    print(list) 
    newlist=[] 
    newlist.append(list[0]) 
    for j in range(len(list)-1):
        newlist.append(list[j]+list[i+1])
    newlist.append(list[-1]) 
    list=newlist