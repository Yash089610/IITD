def AdjList(n, links):
    m = len(links)
    Adj_List = []
    for i in range(n):
        Adj_List.append([])
    for j in range(m):
        Adj_List[links[j][0]].append((links[j][1], links[j][2])) 
        Adj_List[links[j][1]].append((links[j][0], links[j][2]))
    return Adj_List


class Max_Heap:
    def __init__(self, list):
        self.list = list
        self.size = len(list)
        self.indices = [-1]*(len(list))
        for i in range(len(self.list)):
            self.indices[self.list[i][0]] = i 
        self.maxheapify()
        
    def parent(self, i):
        if i>0:
            return (i-1)//2
        return None 

    def left(self, i):
        if 2*i+1 < len(self.list):
            return 2*i+1
        return None 

    def right(self, i):
        if 2*i+2 < len(self.list):
            return 2*i+2
        return None

    def swap(self, i, j):
        self.indices[self.list[i][0]], self.indices[self.list[j][0]] = self.indices[self.list[j][0]], self.indices[self.list[i][0]]
        self.list[i], self.list[j] = self.list[j], self.list[i] 
           

    def maxheapify(self):
        for i in range (self.size-1, -1, -1):
            self.HeapDown(i)

    def HeapDown(self, i):
        val = self.list[i][1]
        left = self.left(i)
        if left != None:
            left_val = self.list[left][1]
            larger = left
            right = self.right(i)
            if right != None:
                right_val = self.list[right][1]
                if right_val > self.list[larger][1]:
                    larger = right
            if val < self.list[larger][1]:
                self.swap(i, larger)
                self.HeapDown(larger)
    

    def HeapUp(self, i):
        val = self.list[i][1]
        parent = self.parent(i)
        if parent != None:
            if val>self.list[parent][1]:
                self.swap(i, parent)
                self.HeapUp(parent)

    def replace(self, i, val):
        old = self.list[i][1]
        if old< val:
            self.list[i] = (self.list[i][0], val)
            self.HeapUp(i)
        else:
            self.list[i] = (self.list[i][0], val)
            self.HeapDown(i)

    def extract_max(self):
        return self.list[0]

    def delete(self, i):
        
        b = self.list[self.size-1][1]
        k = self.list[i][0]
        self.swap(i, self.size -1)
        self.indices[k] = float('inf')
        self.list.pop()
        self.size -= 1
        a = self.parent(i)
        if a != None:
            val = self.list[a][1]
            if val < b:
                self.HeapUp(i)
            else:
                self.HeapDown(i)
        else:
            self.HeapDown(i)

def maxCapList(n, links, s):        #O(nlogn)
    adj_list = AdjList(n, links)
    visited = []
    C = [0]*n   #O(n)
    prev = [None]*n     #O(n)
    v = [False]*n       #O(n)
    list_heap = [(0, 0)]*n      #O(n)
    list_heap[s] = (s, float('inf'))
    for i in range(n):      #O(n)
        if i != s: 
            list_heap[i] = (i, 0)
            i += 1
        else:
            i += 1
    Heap = Max_Heap(list_heap)      #O(n)
    while len(visited) < n-1:
        max = Heap.extract_max()
        curr_node = max[0]
        curr = C[max[0]]
        for i in range(len(adj_list[curr_node])):
            nbrs = adj_list[curr_node]
            w = nbrs[i][0]
            if v[w] == False: 
                cap = nbrs[i][1]
                temp = cap 
                if (v[w] == False) and (curr != 0):
                    temp = min(curr, cap)
                if temp > C[w]:
                    C[w] = temp 
                    prev[w] = curr_node 
                    k = Heap.indices[w]
                    Heap.replace(k, C[w])       #O(logn), happens O(n) times 
        Heap.delete(0)      #O(logn)
        v[curr_node] = True 
        visited.append(curr_node)
    return (C, prev)

def findMaxCapacity(n, links, s, t):        #O(nlogn)
    (Caps, prevs) = maxCapList(n, links, s)
    p = [t]
    curr_prev = t
    while curr_prev != s:
        p.append(prevs[curr_prev])
        curr_prev = prevs[curr_prev]
    return (Caps[t], p[::-1])





                    

            

    

    




        
        
        
        
       