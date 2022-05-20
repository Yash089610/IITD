from typing import List
def sortings(lst : List[str]):
    li=[]
    def q2sortings(inpt : str):
        l=[0]*10
        c=""
        for i in inpt[::-1]:
            if i in "0123456789":
                l[int(i)]+=1
            else:
                c=i
        for i in range(9,-1,-1):
            if l[i]%2==1:
                inpt=str(i)*l[i]+inpt.replace(str(i),"")
        if c!="":
            if inpt[0:inpt.index(c)]!="":
                li.append(int(inpt[0:inpt.index(c)]))
            else:
                li.append(float("inf"))
        else:
            if inpt!="":
                li.append(int(inpt))   
            else:
                li.append(float("inf"))             
        return inpt
    for i in range(len(lst)):
        lst[i]=q2sortings(lst[i])
    return sorted(lst, key=lambda x:li[lst.index(x)])

if __name__=="__main__": # calling main (run automtically)
    lst = []             # list that stores the input strings
    num = int(input())   # taking input from user of number of strings of list
    for i in range(num): # take input of all strings of list
        inpt = input()
        lst.append(inpt) # append each string into the list
    lst = sortings(lst)  # calling function in which you have to write the code
    print (lst)          # printing the output (list of strings) of your's function
