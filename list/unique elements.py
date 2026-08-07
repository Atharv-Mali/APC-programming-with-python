l=[12,13,14,13,11,25,11,25,11]
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
        
print("list :",l)
print("Unique :",unique)