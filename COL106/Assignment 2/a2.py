class PriorityQueue():
    '''Implementation of Priority Queue using Heap.'''

    def __init__(self, data=[]):
        '''Initialise array'''
        self._data = data
        self._index = {}

    def enqueue(self, node):
        '''Enqueue a node'''
        self._data.append(node)
        index = len(self._data)-1
        self._index[node[1]] = index
        self.heapUp(index)

    def heapUp(self, index):
        '''Position the Node properly in the tree by shifting it upwards'''
        while index != 0 and self._data[index] <= self._data[(index-1)//2]:
            self._index[self._data[index][1]] = (index-1)//2
            self._index[self._data[(index-1)//2][1]] = index
            self._data[(
                index-1)//2], self._data[index] = self._data[index], self._data[(index-1)//2]
            index = (index-1)//2

    def existChild(self, index):
        '''Return number of childs of a given node'''
        l = len(self._data)
        if 2*index+1 < (l-1):
            return 2
        elif 2*index+1 == (l-1):
            return 1
        else:
            return 0

    def extractMin(self):
        '''Dequeue the priority node'''
        node = self._data[0]
        self._index.pop(node[1])
        self._data[0] = self._data[-1]
        self._index[self._data[0][1]] = 0
        self._data.pop()
        index = 0
        self.heapDown(index)
        return node

    def heapDown(self, index):
        '''Position the node properly by shifting it downwards'''
        while self.existChild(index) != 0:
            if self.existChild(index) == 2 and (self._data[index] >= self._data[2*index+1+1] or self._data[index] >= self._data[2*index+1]):
                if self._data[2*index+1] >= self._data[2*index+1+1]:
                    self._index[self._data[index][1]] = 2*index+1+1
                    self._index[self._data[2*index+1+1][1]] = index
                    self._data[2*index+1 +
                               1], self._data[index] = self._data[index], self._data[2*index+1+1]
                    index = 2*index+1+1
                else:
                    self._index[self._data[index][1]] = 2*index+1
                    self._index[self._data[2*index+1][1]] = index
                    self._data[2*index +
                               1], self._data[index] = self._data[index], self._data[2*index+1]
                    index = 2*index+1
            elif self._data[index] >= self._data[2*index+1]:
                self._index[self._data[index][1]] = 2*index+1
                self._index[self._data[2*index+1][1]] = index
                self._data[2*index +
                           1], self._data[index] = self._data[index], self._data[2*index+1]
                index = 2*index+1
            else:
                break

    def changeKey(self, index, node):
        '''Change Node data'''
        x = self._data[index]
        self._data[index] = node
        self._index[node[1]] = index
        if x >= node:
            self.heapUp(index)
        if x <= node:
            self.heapDown(index)

    def buildHeap(self):
        '''Build Heap from an unsorted array'''
        for i in range(len(self._data)//2-1, -1, -1):
            self.heapDown(i)
        for i in range(len(self._data)):
            self._index[self._data[i][1]] = i


def coltime(v1, v2, x1, x2, T):
    '''Return time of collision'''
    if v1 > v2:
        return (x2-x1)/(v1-v2)
    else:
        return T+1


def listCollisions(M, x, v, m, T):
    t = 0
    l = []
    ans = []
    '''Pass a list with 9 elements and build heap. 1st element is compared and if its same, 2nd is compared.
    So if collision time is same, 'i' is compared and so we follow left to right traversal order.'''
    for i in range(len(M)-1):
        ti = coltime(v[i], v[i+1], x[i], x[i+1], T)
        l.append([ti, i, x[i]+(v[i]*ti) if v[i] != 0 else x[i], M[i], v[i],
                 x[i], M[i+1], v[i+1], x[i+1], 0])
    p = PriorityQueue(l)
    p.buildHeap()
    '''Time complexity of Build heap is O(n) since we used HeapDown.'''
    while (m > 0 and t <= T):
        # print([[i[:3], i[9]] for i in p._data])
        x = p._data[0]
        vf2 = ((2*x[3]*x[4])-(x[3]-x[6])*x[7])/(x[3]+x[6])
        vf1 = ((2*x[6]*x[7])+(x[3]-x[6])*x[4])/(x[3]+x[6])
        '''Update ith balls data. Time Complexity Omega(log(n)) since we just HeapUp or HeapDown, if needed.'''
        p.changeKey(p._index[x[1]], [T+1, x[1], x[2] + vf1*(T+1), x[3]] +
                    [vf1, x[2], x[6], vf2, x[2], x[0]])
        # If a ball exists on left, update it too
        if x[1] > 0:
            y = p._data[p._index[x[1]-1]]
            ti = coltime(y[4], vf1, y[5]+y[4]*(x[0]-y[9]), x[2], T)
            p.changeKey(p._index[x[1]-1], [x[0]+ti, y[1],
                        x[2] + vf1*ti]+y[3:5]+[y[5]+y[4]*(x[0]-y[9]), y[6], vf1, x[2], x[0]])
        # If a ball exists on right, update it too
        if x[1] < (len(M)-2):
            y = p._data[p._index[x[1]+1]]
            ti = coltime(vf2, y[7], x[2], y[8]+y[7]*(x[0]-y[9]), T)
            p.changeKey(p._index[x[1]+1], [x[0]+ti, y[1],
                        x[2] + vf2*ti, y[3], vf2, x[2]]+y[6:8]+[y[8]+y[7]*(x[0]-y[9]), x[0]])
        m -= 1
        t = x[0]
        '''Round to 4 decimal places'''
        ans.append((float(f"{x[0]:.4f}"), int(x[1]), float(f"{x[2]:.4f}")))
    if len(ans) > 0 and ans[-1][0] > T:
        ans.pop()
    return (ans)


# print(listCollisions([940.1440594570123, 342.32941684559046, 686.1000355388383, 520.8309066514597, 870.9632698994412, 727.2119773442081], [2.5912045650076445, 3.3979994719550377, 5.247957197003846,
#       5.383388625251065, 5.440818809376985, 6.415333653364417], [99.79672039800879, 94.19054127616612, 25.977729855078213, 25.5959601276192, 31.543951443609476, 25.267596192531126], 8, 4.531827813401554))

# Node=[Time,i,Position of collision, m1,v1,x1,m2,v2,x2,last update time]
