Dict = {'Refrigerator':40000, 'TV':50000, 'Smartphone':25000, 'AC':30000}
print(Dict)
Disc = int(input('Enter Discount(%): '))
Total = 0
for i in Dict:
    Total = Dict[i] + Total;
print("Sub-Total: ",Total)
Disc_amt = Total*Disc/100;
print("Total with Discount: ",Total-Disc_amt)