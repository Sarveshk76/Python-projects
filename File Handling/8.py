with open("Que.txt") as file:
    size = len(file.readlines())
    Ans=[]
with open("Que.txt") as file:
    with open("Ans.txt") as file1:
        for i in range(5):
            x = file1.readline(1)
            Ans.append(x)
        for j in range(5):
            for i in range(0,size,5):
                print(file.readline(),end="")
            ans = input('Answer: ')
            if ans == Ans[j]:
                print("Correct")
            else:
                print("Wrong. Answer is ",Ans[j])