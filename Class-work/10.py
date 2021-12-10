u=0
l=0
ch = input('Enter character:')

if(ch.isupper()):
    u=u+1
    print("The Given Character ", ch, "is an Uppercase Alphabet")
elif(ch.islower()):
    l=l+1
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
while ch != '*':
    ch = input('Enter character:')
    if(ch.isupper()):
        u=u+1
        print("The Given Character ", ch, "is an Uppercase Alphabet",u)
    elif(ch.islower()):
        l=l+1
        print("The Given Character ", ch, "is a Lowercase Alphabet")
    else:
        print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
print("Number of Upper case characters: ",u)
print("Number of lower case characters: ",l)