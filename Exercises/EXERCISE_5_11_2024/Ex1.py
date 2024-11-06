n = int(input("Enter a number: "))
a = list()
b = []
for i in range(1,n+1):
     a.append(i);
     b.insert(0,i)


print(tuple(a))
print(tuple(b))