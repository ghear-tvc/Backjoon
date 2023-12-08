word = input()
n = list(set(word.upper())) #set : 중복제거 및 순서랜덤
num = []
for i in n :
    num.append(word.upper().count(i))
max = max(num)
cnt = 0
ind = 0
for i in range(len(num)) :
   if  num[i] == max :
       cnt += 1
       ind = i
if cnt == 1 :
    print(n[ind])
else :
    print('?')