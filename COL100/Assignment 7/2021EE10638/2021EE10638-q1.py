'''
Since we are creating a list with n elements, where we are adding elements at the end, not at any random position,
thus the Time complexity of line 15 is O(n). For line 16-20 its constant O(1) as its basic comparison or changing 
values at specific position in list(This position is constant and doesnt depend on n thus it takes constant time).
Line 21 is a for loop and the number of times it runs depends on n, so its Time complexity is O(n).
Line 22 is basically changing value in list for a constant i so it needs constant time.

Thus time complexity is O(n)+5O(1)+O(n)+O(1)=2O(n)+6O(1) which means complexity is O(n).
'''

from tkinter import N


def heaven(num : int):
    l=[0]*num
    if num==1: return 1
    if num==2: return 2
    if num==3: return 4
    if num>3:
        l[0],l[1],l[2]=1,2,4
        for i in range(3,num):
            l[i]=l[i-1]+l[i-2]+l[i-3]
    return l[num-1]
    
    
if __name__=="__main__": # calling main (run automtically)
    num = int(input())   # taking input from user
    out = heaven(num)    # calling function in which you have written code
    print (out)          # printing the output of your's function
