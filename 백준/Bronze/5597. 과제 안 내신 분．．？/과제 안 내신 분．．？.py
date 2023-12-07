i = list(range(1,31))
for k in range(28) :
    n = int(input())
    i.remove(n)
print(min(i))
print(max(i))