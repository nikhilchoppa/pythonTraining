""" Given a natural number n as input, find the sum of first n natural numbers.
Input
One Integer, denoting n.
Output
One Integer, denoting the required sum.
Example
Input: 5
Output: 15
Explanation:
1+2+3+4+5 = 15 """
#Solution
print("Let's find the sum of the first n natural numbers!!")
n = int(input("Enter a natural number: "))
sum_n = n * (n + 1) / 2
print(f"The sum of the first {n} natural numbers is: {sum_n}")

    
