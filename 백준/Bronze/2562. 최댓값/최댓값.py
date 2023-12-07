a=[]
max = 0 
for i in range(9) :
    a.append(int(input()))
    if max < a[i] :
        max = a[i]
        maxnum = i+1

print(max)
print(maxnum)