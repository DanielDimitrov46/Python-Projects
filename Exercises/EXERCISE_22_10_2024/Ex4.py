import math
prime = True
num = int(input())
for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
        prime = False
        break

if prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")