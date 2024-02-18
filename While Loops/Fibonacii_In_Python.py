# Write a python program using a while loop to print the Fibonacci Series up to the terms.
print("Enter the number for Fibonacci Series:")
num=int(input())
a,b=0,1

i=0
print("The number are in Fibonacci Forms are:")
while (i<num):
    print(a)
    a,b=b,a+b
    i+=1

