from grafo import Grafo


class GrafoLstAdj(Grafo):
    def __init__(self, num_v=0):
        super().__init__(num_v=num_v)
        self.grafo: list[list[int]] = [[] for _ in range(num_v)]
        pass

    def add_vertice(self):
        self.grafo.append([])

    def add_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def arestas(self): # Usado para o copy
        arestas = set()
        for u in range(self.num_v):
            for v in self.grafo[u]:
                if u < v:
                    arestas.add((u, v))
        return arestas

    def remove_vertice(self, u):
        # Remove the vertex u from the adjacency lists of other vertices
        for v in range(self.num_v):
            if u in self.grafo[v]:
                self.grafo[v].remove(u)

        # Adjust the vertex indices for all vertices with a higher index than u
        for v in range(u + 1, self.num_v):
            for w in range(self.num_v):
                if v in self.grafo[w]:
                    self.grafo[w].remove(v)
                    self.grafo[w].append(v - 1)

        # Remove the vertex u from the graph and update the number of vertices
        self.grafo.pop(u)
        self.num_v -= 1

    def remove_aresta(self, u, v):
        self.grafo[u].remove(v)
        self.grafo[v].remove(u)

    def adjs(self, u):
        return self.grafo[u]

    def ha_aresta(self, u, v):
        return v in self.grafo[u]

    def grau(self, u):
        return len(self.grafo[u])

    def tem_alguma_aresta(self, u):
        return len(self.grafo[u]) > 0

