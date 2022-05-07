movie=[]
inp=[]
for _ in range(int(input())): inp.append(input())

def Issue():
    if len(movie)>0: movie.pop(0)
    else: print('Invalid')

def Join(AadharID: int):
    movie.append(AadharID)


def Check():
    if len(movie)>0: print(movie[0])
    else: print('Invalid')

def GetLine():
    if len(movie)>0: print(*movie)
    else: print('Invalid')

for i in inp:
    if 'Join' in i: Join(i.split()[1])
    if 'GetLine' in i: GetLine()
    if 'Check' in i: Check()
    if 'Issue' in i: Issue()