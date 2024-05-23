"""
Geometric_Progression.py
Given first 3 numbers of a geometric progression, predict the next number.
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
a = int(input())
b = int(input())
c = int(input())

ratio = b/a

d = int(ratio * c)
print(d)
