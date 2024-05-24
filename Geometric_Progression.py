"""Given first 3 numbers of a geometric progression, predict the next number.
You can refer to the following link for information about geometric preogression
https://en.wikipedia.org/wiki/Geometric_progression
Input
3 integers should be taken as a input
Output
single integer.
Note: Convert the output to integer
Example
Input:
2
4
8
Output:
16
"""
#Solution 1
def geo(a,b,c):
    cr=b/a
    if c/b==cr:
        gp= a*cr**3
        print(gp)
    else:
        print("Error: The numbers do not form a geometric sequence.")

print("Let's find geometric sequence for given 3 numbers")
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

geo(a,b,c)



    

    