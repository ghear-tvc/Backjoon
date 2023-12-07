row, col = map(int, input().split())
arr = [[0 for j in range(col)] for i in range(row)]
for i in range(row) :
    temp = input().split()
    for j in range(col) :
        arr[i][j] += int(temp[j])
for i in range(row) :
    temp = input().split()
    for j in range(col) :
        arr[i][j] += int(temp[j])
for i in range(row) :
    for j in range(col) :
        print(arr[i][j], end=' ')
    print()