n = int(input())
ll=[]
di={}
for i in range(1,n+1):
    ll.append(i)
    di[i]=ll[len(ll)-1]
print(di)