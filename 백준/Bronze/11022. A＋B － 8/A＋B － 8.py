n = int(input())
for i in range(n) :
    x,y = map(int, input().split())
    print('Case #'+str(i+1)+ ':',x,'+',y,'=',x+y)