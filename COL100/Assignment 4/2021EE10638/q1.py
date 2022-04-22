a,x=int(input()),int(input())
factorial_count=1
for i in range(1,a//x+1):
    factorial_count*=i
print(f"{(x**(a//x))*factorial_count:.2f}")
