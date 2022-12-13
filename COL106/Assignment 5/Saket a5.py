INF = float('inf')

class Graph:
    def __init__(self,n,edge_list):
        #edge_list.sort()
        self.least_in_path = [INF]*n
        self.prev = [None]*n

        self.adj = []
        for i in range(n):
            self.adj.append([0])

        for e in edge_list:
            self.adj[e[0]].append((e[1],e[2]))
            self.adj[e[1]].append((e[0],e[2]))

        for i in range(n):
            self.adj[i].pop(0)


class Heap:
    def __init__(self,n,initial):
        self.n = 50*n
        self.initial_n = n
        self.heap = [None]*self.n
        self.heap[0] = initial
        self.empty_at = 1

    def extract_min(self):
        min = self.heap[0]
        self.heap[0] = (0,0)
        heap_down(self.heap,0,self.empty_at)
        while(self.heap[self.empty_at - 1] == (0,0)):
            self.heap[self.empty_at - 1] = None
            self.empty_at = self.empty_at - 1

        '''
        if(self.empty_at <= (self.n)/2 and self.n > 50*self.initial_n):
            self.n = self.n/2
            heap2 = [None]*(self.n)
            for i in range(self.n):
                heap2[i] = self.heap[i]
            self.heap = heap2
        '''
        return min

    def push(self,node):
        if(self.empty_at == self.n):
            self.n = 2*self.n
            heap2 = [None]*(self.n)
            for i in range(self.empty_at):
                heap2[i] = self.heap[i]
            self.heap = heap2
        
        self.heap[self.empty_at] = node
        heap_up(self.heap,self.empty_at)
        self.empty_at = self.empty_at + 1


def heap_down(list,index,l):
    while(index<l-1):
        parent = list[index]
        left = list[2*index + 1] if 2*index+1<=l-1 else (0,0)
        right = list[2*index + 2] if 2*index+2<=l-1 else (0,0)
        if(left>=right and left>parent):
            list[index] = left
            list[2*index+1] = parent
            index = 2*index + 1
        elif(right>left and right>parent):
            list[index] = right
            list[2*index+2] = parent
            index = 2*index + 2
        else:
            break
    return

def heap_up(list,index):
    while(index>0):
        child = list[index]
        parent = list[(index-1)//2]
        if(parent<child):
            list[(index-1)//2] = child
            list[index] = parent
            index = (index-1)//2
        else:
            break
    return

def least_path(g,s,d):
    l = [d]
    index = d
    while(index!=s):
        l.insert(0,g.prev[index])
        index = g.prev[index]
    return l

def findMaxCapacity(n,edge_list,s,d):

    g = Graph(n,edge_list)
    li = Heap(n,(INF,s))

    g.prev[s] = INF

    while(li.empty_at!=0):
        u = li.extract_min()
        if(u[0]==0):
            break
        u = u[1]
        for pair in g.adj[u]:
            v = pair[0]
            wt = pair[1]
            if(v==g.prev[u]):
                continue
            if (g.least_in_path[v]==INF or min(g.least_in_path[u],wt)>g.least_in_path[v]):
                g.prev[v] = u
                g.least_in_path[v] = min(wt,g.least_in_path[u])
                li.push((wt,v))
                continue
    
    return(g.least_in_path[d],least_path(g,s,d))