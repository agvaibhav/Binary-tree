class MinHeap:

    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return((i-1)//2)

    def heappush(self,k):
        self.heap.insert(0,k)
        self.heapify()

    def heapify(self):
        for i in range(len(self.heap)):
            while(i!=0 and self.heap[self.parent(i)]>self.heap[i]):
                self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]

    def heappop(self):
        return(self.heap.pop(0))

    def decreaseKey(self,i,new_val):
        self.heap[i]=new_val
        self.heapify()

    def extractMin(self):
        res=self.heappop()
        self.heapify()
        return(res)

    def deleteKey(self,i):
        self.decreaseKey(i,float('-inf'))
        self.extractMin()

    def getMin(self):
        return(self.heap[0])

heapObj = MinHeap() 
heapObj.heappush(3) 
heapObj.heappush(2) 
heapObj.deleteKey(1) 
heapObj.heappush(15) 
heapObj.heappush(5) 
heapObj.heappush(4) 
heapObj.heappush(45) 


print(heapObj.extractMin()) 
print(heapObj.getMin())
heapObj.decreaseKey(2, 1) 
print(heapObj.getMin()) 
