#Write a python program using a while loop to calculate the factorail of a number .
print("Enter the number to find factorial:")
num=int(input())
fact=1
a=num
while a>=1:
    fact*=a
    a=a-1
print(f"The factorial of a number {num} is {fact}.")