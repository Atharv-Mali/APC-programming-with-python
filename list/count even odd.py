num=[12,11,32,12,44,1,5,9,12,23,67,66,88,99,7]
even=0
odd=0
for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:",even)
print("Odd numbers:",odd)