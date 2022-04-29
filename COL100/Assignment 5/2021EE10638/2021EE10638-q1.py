def addition(a,b):
    return f"{a+b:.2f}"
def subtraction(a,b):
    return f"{a-b:.2f}"
def multiplication(a,b):
    return f"{a*b:.2f}"
def division(a,b):
    if b==0:
        return "Division by 0 not possible"
    return f"{a/b:.2f}"
def modulus(a,b):
    if b==0:
        return "Modulo by 0 not possible"
    return f"{a%b:.2f}"