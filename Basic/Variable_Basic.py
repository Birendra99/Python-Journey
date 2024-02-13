'''
country='Nepal'
print(country)
print(type(country))
'''

country_name="America" # This is a global variable which is accessible everywhere

def printName():
    name="Sam" #This is a local variable whic can only be access able inside this functions.
    print(name)
    print(country_name)

# print(name)
printName()