from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        num_nodes = len(self.graph)
        visited = [False] * num_nodes
        rec_stack = [False] * num_nodes

        for node in range(num_nodes):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True

        return False

# Example usage:
graph_directed = Graph()
graph_directed.add_edge(0, 1)
graph_directed.add_edge(1, 2)
graph_directed.add_edge(2, 0)
graph_directed.add_edge(2, 3)

if graph_directed.is_cyclic():
    print("Directed Graph has a cycle.")
else:
    print("Directed Graph doesn't have a cycle.")
