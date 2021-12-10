def display(*name, **address):
  for items in name:
    print (items)

  for items in address.items():
    print (items)

#Calling the function
display('Sarvesh')
display(John='LA',Mary='NY',Nina='DC')
display(Sarvesh='MH')