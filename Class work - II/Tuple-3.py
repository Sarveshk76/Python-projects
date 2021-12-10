def my_min(*args):
    result = args[0]
    for num in args:
        if num < result:
            result = num
    return result

x= my_min(4, 5, 6, 7, 2)
print("Minimum element: ",x)