import string
strlist=string.digits+string.ascii_uppercase
strdict={}
c=0
for i in strlist:
    strdict[str(i)]=c
    c+=1

def bastdec(number,frombase):
    ans=0
    for i in range(len(number)):
        ans+=strdict[str(number[::-1][i])]*(frombase**i)
    return ans
        
        
def dectbas(number,tobase,frombase):
    ans=""
    if frombase != 10:
        number=bastdec(str(number),frombase)
    else:
        number=int(number)
    while number>0:
        ans+=str(strlist[number%tobase])
        number=number//tobase
    return ans[::-1]



def radbastdec(number,frombase):
    ans=0
    for i in range(len(number)):
        ans+=float(strdict[str(number[i])]*(frombase**(-1-i)))
    return ans
    


def raddectbas(number,tobase,frombase):
    ans=""
    if frombase != 10:
        number=radbastdec(str(number),frombase)
    else:
        number=float("0."+str(number))
    i=1
    while number>1e-05 and i<=rpoint:
        x=str(number*tobase).split(".")
        ans+=str(strlist[int(x[0])])
        number=float("0."+str(x[1]))
        i+=1
    return ans
        
number=input("Enter the number: ")
tobase=int(input("Enter the base in which the number should be converted: "))
frombase=int(input("Enter the base in which the number is: "))
rpoint=int(input("\nEnter the decimal precision required. \nEnter 0 if input is integer or decimal part not required in output: "))
if rpoint==0:
    x=dectbas(number.split(".")[0],tobase,frombase)
    print("\n")
    print(x)
else:
    x=dectbas(number.split(".")[0],tobase,frombase)
    y=raddectbas(number.split(".")[1],tobase,frombase)
    print("\n")
    print(x,".",y, sep="")