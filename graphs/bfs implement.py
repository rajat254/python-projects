# Dependencies
from collections import defaultdict
from collections import deque


class Graph:
    """ Class to implement Graph Data structure and its associated functions
    like add_edge and BFS. It uses defaultdict Data Structure from
    collections package.
    """
    def __init__(self):
        """Constructor to initialize graph member as a defaultdict."""
        self.graph = defaultdict(list)

    # Function to add Edges in graph
    def add_edge(self, u, v):
        """This function adds vertex to adjacency list. It assumes that
        graph is Bi-Directional"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, source):
        """Function to perform Breadth First Search Traversal. It return a list
        containing the order in which vertices were visited.
        """
        visited = [False] * (vertices + 1)
        queue = deque()
        queue.append(source)
        order = list()
        visited[source] = True
        order.append(source)

        while queue:
            current_node = queue.pop()
            for adjacent_node in self.graph[current_node]:
                if not visited[adjacent_node] :
                    order.append(adjacent_node)
                    visited[adjacent_node] = True
                    queue.append(adjacent_node)

        return order


if __name__ == '__main__':
    test_cases = int(input())
    for test_case in range(test_cases):
        adj_list = Graph()
        vertices, edges = map(int, input().split())

        # Input edges
        for edge in range(edges):
            u, v = map(int, input().split())
            adj_list.add_edge(u, v)

        # here s is the source vertex from which BFS traversal will start
        s = int(input())
        bfs_traversal = adj_list.bfs(s)
        print(bfs_traversal)
