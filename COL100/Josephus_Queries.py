# https://cses.fi/problemset/task/2164/
#I think it works but not efficient enough
for i in range(int(input())):
    inp=input()
    l=[]
    for j in range(int(inp.split()[0])):
        l.append(j+1)
    c=1
    for j in range(len(l)):
        if len(l)==1:
            print(l[0])
            break
        if j+1==int(inp.split()[1]):
            print(l[c])
            break
        l.pop(c)
        c+=1
        if c>(len(l)-1):
            c-=len(l)
        
        
        