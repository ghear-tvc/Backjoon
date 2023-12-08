a = list(input().split())
ades = sorted(a, reverse=True)
aasc = sorted(a, reverse=False)
if a == ades :
    print('descending')
elif a == aasc :
    print('ascending')
else :
    print('mixed')