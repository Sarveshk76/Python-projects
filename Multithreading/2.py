import threading
from threading import *
class new(threading.Thread):
    def run(self):
        for x in range(5):
            print("Child ",current_thread().getName())
obj = new()
obj.start()
obj.join()
print("Returned to ",current_thread().getName())