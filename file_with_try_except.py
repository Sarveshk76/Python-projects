try:
    file = open("random.txt",'w')
    try:
        file.write("Hello")
    except FileNotFoundError:
        print("Error")
    else:
        print("File is Successfully written")
    finally:
        file.close()
except FileNotFoundError:
    print("error")
else:
    print("File is ready for reading")
finally:
    with open("random.txt") as file:
        print(file.readlines())