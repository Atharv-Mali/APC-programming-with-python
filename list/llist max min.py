l=[12, 11, 11, 99, 23, 21, 44, 1, 37]
min=l[0]
max=l[0]
for i in l:
    if(max<i):
        max=i
    if(min>i):
        min=i
print("smallest :",min)
print("largest :",max)
