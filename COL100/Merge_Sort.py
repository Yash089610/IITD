c=[]
def sor(a,b):
    global c
    if len(a)>0 and len(b)>0:
        if a[0]<b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
        sor(a,b)
    elif len(a)==0:
        c.extend(b)
    elif len(b)==0:
        c.extend(a)

def merges(arr):
    global c
    mid=int(len(arr)/2)
    if len(arr)==1:
        b=list(c)
        c=list()
        sor(arr,b)
        return None
    merges(arr[0:mid])
    merges(arr[mid:len(arr)])

merges([1,34,32,76,44,3487,387,3473,4832,328047,508,387,302,47,34,38,487])
print(c)
