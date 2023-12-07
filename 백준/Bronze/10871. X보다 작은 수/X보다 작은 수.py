n, x = map(int, input().split())
a =list( map(int, input().split()))
for i in range(n) :
    if a[i] < x :
        print(a[i], end=' ')

# short code
# n,x=map(int,input().split())
# print(' '.join(i for i in input().split() if int(i)<x))