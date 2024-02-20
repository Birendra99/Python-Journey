#Using Enumerate Object in Loops
#Enumerate() is used with a list called l1. It first prints tuples of index and element pairs. Then it changes the starting index while printing them together. Finally, it prints the index and element separately, each on its own line.

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
	print (ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
	print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
	print(count)
	print(ele)
