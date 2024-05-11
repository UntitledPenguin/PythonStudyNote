import heapq

class Graph:
    def __init__(self):
        self.nodes = set() # initializing a set to store the node code
        self.edges = {} # initializing edge as empty dictionary
        
    def add_node(self, value):
        self.nodes.add(value) # constructing nodes according to the starting and ending point of edge 
        if value not in self.edges: 
            self.edges[value] = {}
        
    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node) 
        self.add_node(to_node)
        self.edges[from_node][to_node] = weight # Supposing we are dealing with direct graph        
   
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes} #initializing the shortest distance as infinite
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            #if current_distance > distances[current_node]: 
                #continue
            for neighbor, weight in self.edges[current_node].items(): #Search at the frontier of the explored graph to find a new Dijkstra edge
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor)) # Add all the new node linked to the explored path into the heap(the expansion of the frontier)
        return distances

# Example usage:
g = Graph()
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 3)
g.add_edge('A', 'E', 5)
g.add_edge('C', 'F', 2)
g.add_edge('C', 'D', 4)
g.add_edge('C', 'E', 2)
g.add_edge('E', 'G', 1)
g.add_edge('B', 'G', 3)
g.add_edge('F', 'G', 2)
g.add_edge('D', 'F', 2)
g.add_edge('D', 'H', 1)
g.add_edge('H', 'F', 3)
g.add_edge('H', 'G', 3)
g.add_edge('G', 'H', 1)
print(g.dijkstra('A'))