'''Extreme Product
You have been given n integer values. You have to find their extreme product.
Extreme product is defined as the product of the two extreme values in the given input, that is maximum and minimum.
Input Format:
First line denotes n, the number of inputs. The next n lines contains one integer in each line.
Output Format:
One integer denoting the extreme product of the given n values.
Example:
Input:
5
10
20
30
40
50
Output:
500
'''
n=int(input("enter the number of values"))
inputs=[]
for i in range(n):
    inputs.append(int(input(f"enter the value { i+1}")))
inputs.sort()
ep=inputs[0]*inputs[-1]
print(f"ep is {ep}")