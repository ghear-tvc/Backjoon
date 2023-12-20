inp = int(input())
for i in range(inp) :
   b = input()
   a = [0 for i in range(len(b))]
   # print(b[4])
   for j in range(len(b)) :
      if b[j] == 'O' :
         a[j] = 1
         if j>0 and b[j]==b[j-1]=='O' :
            a[j]=a[j-1]+1
   print(sum(a))