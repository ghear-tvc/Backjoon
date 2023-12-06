a = list(map(int, input().split()))
a.sort(reverse=True)
if a[0] == a[1] and a[0] == a[2] :
    print(10000+a[0]*1000)
elif a[0] != a[1] and a[1] != a[2] :
    print(a[0]*100)
else :
    print(1000 + a[1]*100)
