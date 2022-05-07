plate=[]
inp=[]
for _ in range(int(input())): inp.append(input())
    
def PickPlate():
    if len(plate)>0: plate.pop(0)
    else: print('Invalid')

def AddPlate(PlateID: int):
    plate.insert(0,PlateID)

def Check():
    if len(plate)>0: print(plate[0])
    else: print('Invalid')

for i in inp:
    if 'AddPlate' in i: AddPlate(i.split()[1])
    if 'PickPlate' in i: PickPlate()
    if 'Check' in i: Check()