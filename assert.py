def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0)
   return ((Temperature-273)*1.8)+32
try:
    KelvinToFahrenheit(-5)
except AssertionError:
    print("Colder than absolute zero!")

i=0
x = {i : i for i in range(5)}
print(x)
y = [i for i in range(5)]
print(y)