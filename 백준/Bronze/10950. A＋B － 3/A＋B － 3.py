i = 0
a = int(input())
x=[]
while i < a :
    x.append(str(sum(map(int, input().split()))))
    i += 1 
i = 0
while i < a :
    print(x[i])
    i += 1 