'''
Given a natural number n as input, find the sum of first n natural numbers.
Input
One Integer, denoting n.
Output
One Integer, denoting the required sum.
Example
Input: 5
Output: 15
Explanation:
1+2+3+4+5 = 15
'''
a=int(input())
sum=0
for i in range(a+1):
    sum+=i
    
print(sum)
