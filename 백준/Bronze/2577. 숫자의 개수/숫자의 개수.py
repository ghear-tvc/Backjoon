p = 1
for i in range(3) :
    p *= int(input())
for i in range(10) :
    print(str(p).count(str(i)))