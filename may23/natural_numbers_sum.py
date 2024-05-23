"""
natural_numbers_sum.py
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

"""
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i  # sum = sum+i
print(sum)
