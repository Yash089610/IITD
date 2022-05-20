# https://cses.fi/problemset/task/1072/
for i in range(1,int(input())+1):
    c=48+8*(i-4)*(i+1)        
    print(int((i**2*(i**2-1)-c)/2))