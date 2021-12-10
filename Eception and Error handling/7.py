try:
    file = open("file.txt",'w')
    file.write("D. Y. Patil Institute of Master of Computer Applications and Management")
    file.close()
    with open("file.txt",'r') as file1:
        print(file1.read())
        raise EOFError
except EOFError:
    print("Reached the End Of File.")