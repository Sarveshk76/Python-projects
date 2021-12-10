def fun_name():
    num=2
    while True:
        yield num
        num+=2
f1=fun_name()
for i in range(1,11):
    print(next(f1))