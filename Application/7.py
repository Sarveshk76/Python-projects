def validate_creditcard(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

x = ["4532015112830366","4532015112812343"]
for i in range(len(x)):
    if validate_creditcard(x[i])==0:
        print(x[i],": Valid credit card number")
    else:
        print(x[i],": Invalid credit card number")