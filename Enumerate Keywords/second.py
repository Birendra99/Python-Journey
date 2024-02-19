#Here, we are using the enumerate() function with both a list and a string. Creating enumerate objects for each and displaying their return types. It also shows how to change the starting index for enumeration when applied to a string, resulting in index-element pairs for the list and string.

'''
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

'''

l1=["Ram","Siat","Hair","Gita"]
name="Birendra"

obj1=enumerate(l1)
obj2=enumerate(name)

#Check the type of the enumerate
print(f"Type: {type(obj1)}")

print(list(enumerate(l1)))

# Starting the index from 2
print(list(enumerate(name,2)))