from heapq import heappush
from heapq import heappop


class Graph:
    def __init__(self):
        self.nodes = {}  # identifier: (edge, weight) pairs

    def read_input(self):
        nb_nodes, nb_edges = map(int, input().split())
        for i in range(1, nb_nodes + 1):
            self.nodes[i] = []
        for _ in range(nb_edges):
            edge1, edge2, weight = map(int, input().split())
            self.nodes[edge1].append((edge2, weight))
            self.nodes[edge2].append((edge1, weight))

    def prim(self):
        visited = set()
        heap = []  # (weight, identifier)
        total_weight = 0
        heappush(heap, (0, 1))
        while (len(heap) != 0):
            weight, min_id = heappop(heap)
            if (min_id not in visited):
                total_weight += weight
                visited.add(min_id)
                for (neighbor, weight) in self.nodes[min_id]:
                    if (neighbor not in visited):
                        heappush(heap, (weight, neighbor))
        return total_weight


graph = Graph()
graph.read_input()
print(graph.prim())
