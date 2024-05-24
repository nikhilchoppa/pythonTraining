""" Given two integers a and b denoting the two angles of a triangle (in degrees), find the third angle of the triangle (in degrees).
Note: The given angles will always be of a valid triangle.
Input
First line contains an integer denoting a, the first angle.
Second line contains an integer denoting b, the seocnd angle.
Output
One Integer, denoting the third angle of the triangle.
Example
Input:
30
110
Output:
40 """

print("Let's find the third angle in a triangle when you specify two of them")
a= int(input("Enter the first angle: "))
b= int(input("Enter the second angle: "))
d= a+b
if d<180:
    e=180-d
    print(e)
else:
    print("Given sum of angle exceeds 180 so it cannont form a triangle. The sum all three angles in a triangle should be equivalent to 180")

