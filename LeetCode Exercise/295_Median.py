import heapq

class MedianFinder(object):

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]

    def addNum(self, num):
        """
        :type num: float
        :rtype: None
        """
        if not self.minheap or num<self.minheap[0]:
            heapq.heappush(self.maxheap,-num) 
        else:
            heapq.heappush(self.minheap,num) 
        
        #rebalance
        if len(self.maxheap)-len(self.minheap)>1:
            heapq.heappush(self.minheap,heapq.heappop(self.maxheap)*(-1))
        elif len(self.minheap)>len(self.maxheap):
            heapq.heappush(self.maxheap,heapq.heappop(self.minheap)*(-1))   

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.maxheap and not self.minheap:
            return(None)
        if self.maxheap or self.minheap:
           if len(self.maxheap)>len(self.minheap):
                self.median=self.maxheap[0]*(-1)
           elif len(self.maxheap)<len(self.minheap):
                self.median=self.minheap[0]
           else:
            self.median=(self.maxheap[0]*(-1)+self.minheap[0])/2.0
        return(self.median)


obj = MedianFinder()
a=[[199],[197],[196],[195],[194],[188],[186],[184],[181],[180],[176],[175],[174],[173],[171],[170],[169],[168],[167],[166],[164],[160],[158],[157],[156],[155],[154],[153],[152],[148],[147],[145],[143],[142],[141],[139],[138],[137],[136],[135],[134],[133],[132],[131],[130],[126],[125],[122],[119],[118],[112],[111],[108],[105],[104],[102],[101],[100],[99],[97],[96],[95],[94],[88],[87],[86],[85],[84],[83],[79],[78],[77],[75],[73],[72],[71],[68],[67],[64],[61],[60],[59],[58],[57],[56],[53],[52],[46],[44],[43],[40],[39],[34],[28],[26],[25],[24],[23],[21],[20],[19],[18],[17],[11],[10],[9],[8],[6],[5],[3],[2],[1],[-1],[-3],[-6],[-7],[-9],[-12],[-13],[-18],[-19],[-20],[-25],[-26],[-27],[-32],[-33],[-38],[-39],[-42],[-43],[-44],[-45],[-47],[-48],[-50],[-51],[-52],[-55],[-57],[-58],[-60],[-62],[-64],[-65],[-66],[-67],[-71],[-77],[-80],[-83],[-84],[-85],[-86],[-88],[-89],[-91]]
for nx in a:    
    obj.addNum(nx[0])

param_2 = obj.findMedian()
