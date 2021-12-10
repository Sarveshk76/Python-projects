name=input("Enter Your Name \t\t\t\t: ")
vname=input("Enter vehicle Name \t\t\t\t: ")
vnum=input("Enter Your vehicle Number \t\t: ")
last_oc = 2500;
next_oc = 5000;
curr_oc = int(input("Enter current number of miles: "))
print("Name\t\t\t\t\t:",name)
print("Vehicle Name\t\t\t:",vname)
print("Vehicle Number\t\t\t:",vnum)
print("Last oil change milage\t:",last_oc," KMs.")
if(curr_oc >= next_oc):
    print("Your vehicle need an immidiate oil change.")
else:
    print("Your vehicle need an oil change after ",next_oc-curr_oc," KMs.")