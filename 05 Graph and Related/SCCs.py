from collections import deque

class Graph:
    def __init__(self,n) -> None:
        self.n=n
        i=0
        self.u = [[] for _ in range(n+1)]
        self.rev_u = [[] for _ in range(n+1)]
        while i<n:
            i=i+1
            self.u[i]=[]
        
    def add_Edge(self,a,b):
        self.u[a].append(b)
        self.rev_u[b].append(a)

    def dfs_rev(self,nodex):
        self.explored[nodex]=True
        for j in self.rev_u[nodex]: 
            if not self.explored[j]: self.dfs_rev(j)
        self.stack.appendleft(nodex)
    
    def dfs(self,nodex):
        self.explored[nodex]=True
        for j in self.u[nodex]: 
            if not self.explored[j]: self.dfs(j)
        self.s.append(nodex)
    
    def printscc(self):
        #DFS reversed G:
        f=[]
        self.explored = [False] * (self.n + 1)
        self.stack=deque() #finishing time
        
        #first pass:
        for i in range(1,self.n+1):
            if not self.explored[i]: self.dfs_rev(i)
        print("finishing time:",self.stack)
        
        self.explored = [False] * (self.n + 1)
        #second pass:
        self.scc=[]
        for v in self.stack:
            if not self.explored[v]:
                self.s=[]
                self.dfs(v)
                self.scc.append(self.s)
        print(self.scc)

    
G=Graph(9)
G.add_Edge(1,4)
G.add_Edge(7,1)
G.add_Edge(4,7)
G.add_Edge(9,7)
G.add_Edge(9,3)
G.add_Edge(6,9)
G.add_Edge(3,6)
G.add_Edge(8,6)
G.add_Edge(2,8)
G.add_Edge(8,5)
G.add_Edge(5,2)
print (G.u)
print (G.rev_u)
G.printscc()

