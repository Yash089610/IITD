x=float(input())
n=int(input())
for i in range(1,n+1):
    print(f"{(-1)**i/(x**(2*i)):.2f}")