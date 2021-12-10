from threading import *
def print_hello(n):
    i=0
    while i!=n:
        print("Hello, how old are you ", current_thread().getName())
        i+=1
t1 = Thread( print_hello(5))

t1.start()
t1.join()
print(current_thread().getName())
print("Bye")