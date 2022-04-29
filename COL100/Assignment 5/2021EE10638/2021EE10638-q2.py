def factorial(a):
    if a in (0,1):
        return f"{1:.2f}"
    if a<0:
        return "Don't enter a negative number"
    return f"{(a*float(factorial((a-1)))):.2f}"

print(factorial(int(input())))