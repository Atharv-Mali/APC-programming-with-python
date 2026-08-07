city=["delhi","mumbai","kolhapur","pune","latur","nagpur","satara"]
c=input("Enter city :")
found=False
for i in city:
    if c==i:
        found=True
        break
if found:
    print(c,"is present in list")
else:
    print(c,"is not present in list")