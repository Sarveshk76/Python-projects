email=input("Enter Your Email id : ")
print("Your Original Email id is : ",email)
dom=email[email.index('@')+1:]
user=email.replace(dom,'').replace('@','')
print("User name is : ",user)
print("Domain name is : ",dom)