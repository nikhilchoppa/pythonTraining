'''
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
