a = int(input())
b = int(input())
s = 0
i = 0
while i < b :
    n1, n2 = (map(int, input().split()))
    s += n1*n2
    i+=1
if a == s :
    print('Yes')
else :
    print('No')