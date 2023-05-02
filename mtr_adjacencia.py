import graphviz

from grafo import Grafo


class GrafoMtrAdj(Grafo):
    def __init__(self, num_v=0):
        super().__init__(num_v=num_v)
        self.grafo = [[0 for _ in range(num_v)] for _ in range(num_v)]

    def add_vertice(self):
        self.grafo.append([0 for _ in range(self.num_v)])

    def add_aresta(self, u, v):
        self.grafo[u][v] += 1
        self.grafo[v][u] += 1

    def arestas(self):
        arestas = set()
        visited = [False] * self.num_v
        for u in range(self.num_v):
            visited[u] = True
            for v in self.adjs(u):
                if not visited[v]:
                    arestas.add((u, v))
        return arestas

    def remove_vertice(self, u):
        self.grafo.pop(u)
        for v in self.grafo:
            v.pop(u)
        self.num_v -= 1

    def remove_aresta(self, u, v):
        self.grafo[u][v] -= self.grafo[u][v]
        self.grafo[v][u] -= self.grafo[v][u]

    def adjs(self, u):  # O(V)
        return [v for v in range(self.num_v) if self.grafo[u][v] > 0]

    def ha_aresta(self, u, v):
        return self.grafo[u][v] > 0

    def grau(self, u):
        return sum(self.grafo[u])

    def tem_alguma_aresta(self, u):  # O(V)
        for i in self.grafo[u]:
            if i > 0:
                return True
