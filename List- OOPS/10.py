import time
class timer:
    def __init__(self,s):
        self.s=s
    def __iadd__(self, other):
        self.s = self.s + other.s
        return timer(self.s)
    def display(self):
        time.sleep(1)
        print(self.s,"s")

obj = timer(1)
obj1 = timer(0)
Input=int(input("Set timer(in sec): "))
for i in range(Input):
    obj1 += obj
    obj1.display()
