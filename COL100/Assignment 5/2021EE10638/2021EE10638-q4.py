l=[]
def numwords(l):
    return len(str(min(l,key=lambda v: len(str(v).replace("\"","").replace(","," ").replace("."," ").split()))).replace("\"","").replace(","," ").replace("."," ").split())
for i in range(int(input())):
    l.append(input())
print(f"{numwords(l):.2f}")