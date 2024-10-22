n = int(input())
ll = []
for i in range(n):
    num = int(input())
    ll.append(num)
max = ll[0]
for i in ll:
    if i > max:
        max = i

print(max)