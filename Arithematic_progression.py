"""Arithmetic_Progression.py
Given first 3 number of a arthimetic progression, predict the next number.
For details about arithmetic progression, you can visit the following link https://en.wikipedia.org/wiki/Arithmetic_progression
Input
3 integers, each should be taken as a input
Output
single integer
Example
Input:
2
5
8
Output:
11 """

print("Let's find arithematic progression using 3 numbers")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d= b-a
e= c-b
if d==e :
    f=c+e
    print(f)
else:
    print("Cannot find the next number because the common difference in not equal.")
    
