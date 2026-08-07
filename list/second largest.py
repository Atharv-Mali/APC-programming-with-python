l=[12,22,44,67,1,7,3,88]
large=l[0]
slarge=-1
for i in l:
    if(i>large or slarge<i):
        slarge=large
        large=i

print("Second largest :",slarge)
        
    