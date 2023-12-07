for i in range(int(input())) :
    a = list(map(str, input().split()))
    for k in range(len(a[1])) :
        print(a[1][k]*int(a[0]), end='')
    print()