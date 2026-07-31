import math
n = int(input("Enter a number: "))
sq=int(math.sqrt(n))
if sq <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, sq):
        if sq % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
    
    