def getStack():
    stack = []
    return stack
def isempty(stack):
    if stack == []:
        return True
    else:
      return False
def Top(stack):
    if isempty(stack):
        return None
    else:
      print("The item at the top is ","'",stack[len(stack) - 1],"'")
def Push(stack, item):
    stack.append(item)
    print(item, " is pushed into the stack")
def Pop(stack):
    if isempty(stack):
        return None
    else:
      item = stack[len(stack) - 1]
      del stack[len(stack) - 1]
      return item
      print(item," is popped out of the stack")