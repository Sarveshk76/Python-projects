name=input("Enter a String : ")
obj=iter(name)
while True:
    try:
        item=next(obj)
        print(item)
    except StopIteration:
        break