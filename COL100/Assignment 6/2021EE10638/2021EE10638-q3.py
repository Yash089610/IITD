order=[]
bill=[]
inp=[]
for _ in range(int(input())): inp.append(input())
def Highest():
    if len(order)>0: print(order[bill.index(max(bill))])
    else: print('Invalid')

def Order(orderID, BillValue):
    order.append(int(orderID))
    bill.append(int(BillValue))

def Serve():
    if len(order)>0: order.pop(bill.index(max(bill))) and bill.pop(bill.index(max(bill)))
    else: print('Invalid')

for i in inp:
    if 'Order' in i: Order(i.split()[1],i.split()[2])
    if 'Serve' in i: Serve()
    if 'Highest' in i: Highest()