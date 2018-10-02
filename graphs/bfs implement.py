from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)#defualt dictionary
    def add_edge(self,u,v):#adding edge in graph
        self.graph[u].append(v)
        self.graph[v].append(u)
    def BFS(self,s):#bfs fuction
        
        visited=[False]*(n+1)#to check vertice is visited or not
        queue=[]
        queue.append(s)
        distance=[0]*(n+1)#if distance asked assuming unit distance(1)
        
        while(queue):
            s=queue.pop(0)
            for  i in self.graph[s]:
                if visited[i]!=True:
                    
                    distance[i]=distance[s]+1
                    visited[i]=True
                    queue.append(i)
        return (distance)            
g=Graph()
q=int(input()) 
for x in range(q):
    g=Graph()
    ne=input().split()
    
    n=int(ne[0])#number of nodes
    e=int(ne[1])#number of edges
    for i in range(e):
        uv=input().split()
        u=int(uv[0])#nodes between edge
        v=int(uv[1])
        
        g.add_edge(u,v)
    s=int(input())#for traversing or finding shortest distance form s to all nodes
    
    t=g.BFS(s)
          
    
