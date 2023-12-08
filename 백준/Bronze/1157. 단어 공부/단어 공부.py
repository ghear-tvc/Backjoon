word = input().upper()
cnt =0
for i in set(word) :
    if word.count(i) > cnt :
        cnt = word.count(i)
        d = i
    elif word.count(i) == cnt:
        d = '?'
print(d)