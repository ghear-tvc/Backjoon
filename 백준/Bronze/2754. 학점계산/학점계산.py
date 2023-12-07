grade = input()
if grade.startswith('A') :
    t =4.0
elif grade.startswith('B') :
    t = 3.0
elif grade.startswith('C') :
    t = 2.0
elif grade.startswith('D') :
    t = 1.0
else :
    t = 0.0
 
if grade.endswith('+') :
    print(t+0.3)
elif grade.endswith('-') :
    print(t-0.3)
else :
    print(t)