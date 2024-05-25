'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward
Input
1 containing integer
Output
1 line containing either "True" or "False"
Example
Input: 121
Output: True
Input: 10
Output: False
'''
a=input("enter number:")
if a==a[::-1]:
    print("given number is a palindrome")
else:
    print("not a palindrome")

