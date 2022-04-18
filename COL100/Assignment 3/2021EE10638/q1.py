a,b,c=float(input()),float(input()),float(input())
if a>=b:
    if a>=c:
        print(f"{a:.2f}")
    else:
        print(f"{c:.2f}")
elif b>=c:
    print(f"{b:.2f}")
else:
    print(f"{c:.2f}")