import math
for i in range(int(input())) :
    a, b, c = map(int, input().split())
    x = math.ceil(c/a) #YYXX
    if c%a == 0 :
        y = a
    else :
        y = c%a
    sx = str(x)
    if x < 10 :
        sx = '0'+ str(x)
    print(str(y)+sx) 