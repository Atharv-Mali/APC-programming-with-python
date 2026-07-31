n=int(input("Enter N value :"))
sum=1
fact=1
for i in range(1,n+1):
    fact*=i
    sum+=(1//fact)
    
print(sum)