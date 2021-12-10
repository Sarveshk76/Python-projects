def calculate(distance,no_of_passengers):
    cost = 0
    cost = 70 * distance/10
    rest = 0
    rest = no_of_passengers * 80
    if cost <= rest :
        return abs(cost - rest)
    else :
        return -1
distance=[20,30,45,55]
no_of_passengers=[50,42,30,33]
print()

for i in range(4):
    print("Distance(km): ",distance[i])
    print("No. of passangers: ",no_of_passengers[i])
    print("Profit earned: ",calculate(distance[i],no_of_passengers[i]))