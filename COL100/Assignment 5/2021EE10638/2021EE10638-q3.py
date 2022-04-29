def padovan(a):
    if a in (0,1,2):
        return f"{1:.2f}"
    return f"{(float(padovan((a-2)))+float(padovan((a-3)))):.2f}"
print(padovan(int(input())))
