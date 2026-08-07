l=[]
i=1
while i<=10:
    ele=int(input("Enter number :"))
    l.append(ele)
    i+=1
print(l)
sum=0
for i in l:
    sum+=i
average=sum/10
print("Sum :",sum)
print("Average :",average)