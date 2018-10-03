'''Author-Rajat Pal
Email-pal.rajat1997@gmail.com)'''
#this is program for krushkal algorithim to find minimum spanning tree using disjoini sets union method
class Graph:

    def __init__(self,tnodes):
        
        self.parent=[0]*(tnodes+1)
        self.rank=[0]*(tnodes+1)
        for x in range(1,tnodes+1):
            
            self.parent[x]=x
    def findset(self,data):
        
        if self.parent[data]==data:
            return data

        return self.findset(self.parent[data])
    def union(self,data1,data2):#for union of two sets
        
        par_data1=self.findset(data1)
        par_data2=self.findset(data2)
        if par_data1==par_data2:
            self.rank[par_data1]=1
            pass
        else:
            
            self.distance+=p[(data1,data2)]
            
            if self.rank[par_data2]>self.rank[par_data1]:
                par_data1,par_data2=par_data2,par_data1
            self.parent[par_data2]=par_data1    
            
            
g_n,g_e=list(map(int,input().split()))#g_n is number of nodes and g_e is number of edges

g=Graph(g_e)
g.distance=0#sum of weight of final mst
p=dict()
for i in range(g_e):
    u,v,weight=list(map(int,input().split()))
    if (u,v) in p:
        if p[(u,v)]>weight:
            p[(u,v)]=weight
    else:
        p[u,v]=weight

        
p=dict(sorted(p.items(),key=lambda x:x[1])) # for sorting edges according to minimum weight  
for items in p:
    g.union(items[0],items[1])
print(g.distance)
