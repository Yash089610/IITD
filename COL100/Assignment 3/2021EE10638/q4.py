a=input()
b=len(a)
if b==1:
    print("YES")
if b==2 or b==3:
    if a[0]==a[-1]:
        print("YES")
    else:
        print("NO")
if b==4:
    if a[0]==a[-1] and a[1]==a[-2]:
        print("YES")
    else:
        print("NO")