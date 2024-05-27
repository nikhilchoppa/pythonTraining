bw=2
sw=15*bw
ow=10*sw
w=0
basket=input()
for char in basket:
    if char=='b':
        w+=bw
    if char=='o':
        w+=ow
    if char=='s':
        w+=sw
print(w)