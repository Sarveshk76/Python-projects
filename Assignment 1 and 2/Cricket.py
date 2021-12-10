import random
FYMCA = 0
COMPUTER = 0
COMPUTER = random.randrange(30,50)
for j in range(1,11):
    for i in range(1,31):
        runs = random.randrange(0,6)
        if(runs == 0):
            break
        else:
            FYMCA = FYMCA + runs
print("COMPUTER: ",COMPUTER);
print("DYPIMCA: ",FYMCA);

if FYMCA>COMPUTER:
    print("Winner : FYMCA")
else:
    print("Computer : Winner")