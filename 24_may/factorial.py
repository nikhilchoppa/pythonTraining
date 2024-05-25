'''Description
Write a program that computes the factorial of a given integer. Your implementation should be iterative in nature. Factorial of an integer n is defined as Factorial(n) = 1*2*3*....*(n-2)*(n-1)*n. Factorial(0) is defined as 1. Factorial of a negative integer is undefined.
Input format
One line containing an integer n.
Output format
One line containing the factorial of n.
Sample input
5
Sample output
120
'''
a=int(input("enter number:"))
fact=1
i=1
if a==0:
        print(fact)
elif a>0:
    while i<=a:
    
        fact=fact*i
        i+=1
    print(fact)
else:
     print("undefined")
     
    


