class heap:
    def __init__(self,array,n):
        self.pos=[i for i in range(n)]
        self.array=array
        self.size=n
    
    def exist(self,index):
        return self.pos[index]
    def compare(self, ii, jj): 
        
        
        return self.array[ii][1] > self.array[jj][1]
        
    
    def swap_index(self, ii, jj):
        self.array[ii], self.array[jj] = self.array[jj], self.array[ii]
        self.pos[self.array[ii][0]] = ii
        self.pos[self.array[jj][0]] = jj
        
    def upheap(self,index):
        parent =(index-1)//2
        if parent>=0:
            if self.compare(index,parent):
                self.swap_index(parent,index)
                self.upheap(parent)
    
    def downheap(self,n):
        left=2*n+1
        right=2*n+2
        if left<self.size:
            big=left
            if right<self.size:
                if self.compare(right,left):
                    big=right
            if self.compare(big,n):
                self.swap_index(big,n)
                self.downheap(big)
    def rem_max(self):
        self.swap_index(0,self.size-1)
        give=self.array.pop()
        self.pos[give[0]]="_"
        self.size-=1
        self.downheap(0)
         
        return give    
    def update(self,n,value):
        index=self.pos[n]
        self.array[index][1]=value
        self.upheap(index)
        
    
        
class construct:
    def __init__(self,array,n):
        self.adj_list=[[] for i in range(n)]
        for i in array:
            s,t,c=i[0],i[1],i[2]
            self.adj_list[s].append((t,c))
            self.adj_list[t].append((s,c))
            
        #print(self.adj_list[30],999999999)
    def searcher(self,n,source,sink):
        result=[]
        give=[]
        for i in range(n):
            result.append([i,0])
            give.append([[i],0])
        #print(result,give)
        max_heap=heap(result,n)
        max_heap.update(source,2**30)
        give[source][1]=2**30
        # print(max_heap.array)
        # print(give)
        while max_heap.size:
            #print(give)
            current=max_heap.rem_max()
            cr_index=current[0]
            current_capacity=current[1]
            current_path=give[cr_index][0]
            #print(cr_index,current_capacity,current_path)
            #print(current_path)
            for i in self.adj_list[cr_index]:
                index=i[0]
                capacity=i[1]
                #print(index,capacity,9990000,give[index][1])
                #print(max_heap.pos)
                if max_heap.exist(index) !="_" and capacity>give[index][1] and current_capacity>give[index][1]:
                    #print(99999999999)
                    update=min(current_capacity,capacity)
                    give[index]=[current_path+[index],update]
                    max_heap.update(index,update)
        ans=give[sink]
        return (ans[1],ans[0])
def findMaxCapacity(n,links,s,t):
    line=construct(links,n)
    return line.searcher(n,s,t)
# print( findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1))
# print( findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))




        

