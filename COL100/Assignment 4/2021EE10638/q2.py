x=int(input())
for i in range(x):
    if i==0 or i==x-1:
        print("*"*x)
    else:
        print("*"+" "*(x-2)+"*")
