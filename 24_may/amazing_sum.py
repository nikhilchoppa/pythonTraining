'''
You have been given n integer values. Lets say the given values are 
a
1
𝑎1
, 
a
2
𝑎2
, 
a
3
𝑎3
, 
a
4
𝑎4
 ... 
a
n
𝑎𝑛
If the sum of two consecutive input values is greater than 100, then the given values have amazing sum
Input Format:
First line denotes n, the number of inputs. The next n lines contains one integer in each line.
Output Format:
One string, either true or false, denoting whether the given values has amazing sum or not.
Example:
Input:
5
20
12
23
41
17
Output:
false'''


n=int(input("enter number of inputs:"))
a=[]

for i in range(n):
    a.append(int(input(f"enter number{i+1}:")))


for i in range(len(a)-1):
    
        if((a[i]+a[i+1])<100):
            res='false'
        else:
            res='true'
            break

print(res)