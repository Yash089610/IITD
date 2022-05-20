def sortings(inpt : str):
    l=[0]*10
    for i in inpt:
        if i in "0123456789":
            l[int(i)]+=1
    for i in range(9,-1,-1):
        if l[i]%2==1:
            inpt=str(i)*l[i]+inpt.replace(str(i),"")
    return inpt

if __name__=="__main__": # calling main (run automtically)
    inpt = input()       # taking input from user (string type)
    out = sortings(inpt) # calling function sortings in which you have to write code
    print (out)          # printing the output of your's function

    
            
    
            
            