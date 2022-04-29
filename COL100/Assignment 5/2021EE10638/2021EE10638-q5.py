def pattern(a):
    if a==1:
        return 111
    return((str(a)+str(pattern(a-1)))*2+str(a))
print(pattern(int(input())))