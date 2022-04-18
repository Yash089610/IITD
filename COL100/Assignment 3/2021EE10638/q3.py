a,b,c=float(input()),float(input()),float(input())

if (b**2-4*a*c)>=0:
    print(f"{(-b+(b**2-4*a*c)**(0.5))/(2*a):.2f}","0")
    print(f"{(-b-(b**2-4*a*c)**(0.5))/(2*a):.2f}","0")
else:
    print(f"{(-b/(2*a)):.2f}", f"{(4*a*c-b**2)**(0.5)/(2*a):.2f}")
    print(f"{(-b/(2*a)):.2f}", f"{-(4*a*c-b**2)**(0.5)/(2*a):.2f}")