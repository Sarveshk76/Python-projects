import random
player1=0
player2=0
for i in range (1,21):
    if i%2==1:
        n=0
        n = random.randrange(1, 7, 1)
        player1 = player1 + n
        print("Player1: ", n)
        while(n==4 or n==6):
            n=0
            n = random.randrange(1, 7, 1)
            player1 =player1 + n
            print("Bonus Round: ")
            print("Player1: ", n)
    else:
        n=0;
        n = random.randrange(1, 7, 1)
        player2 =player2 + n
        print("Player2: ", n)
        while(n == 4 or n == 6):
            n=0
            n = random.randrange(1, 7, 1)
            player2 =player2 + n
            print("Bonus Round: ")
            print("Player2: ", n)

print("Player1 score: ",player1)
print("Player2 score: ",player2)