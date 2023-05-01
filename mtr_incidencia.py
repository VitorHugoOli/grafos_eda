from grafo import Grafo


class GrafoMtrInc(Grafo):
    def __init__(self, num_v=0):
        super().__init__(num_v=num_v)
        self.grafo: list[list[int]] = [[] for _ in range(num_v)]
        self.num_a = 0

    def add_vertice(self):
        self.grafo.append([])
        self.num_v += 1

    def add_aresta(self, u, v):
        self.grafo[u].append(1)
        self.grafo[v].append(1)
        for i in range(self.num_v):
            if i != u and i != v:
                self.grafo[i].append(0)
        self.num_a += 1

    def arestas(self):
        arestas = set()
        for u in range(self.num_v):
            for i, value in enumerate(self.grafo[u]):
                if value > 0:
                    for j in range(u + 1, self.num_v):
                        if self.grafo[j][i] > 0:
                            arestas.add((u, j))
        return arestas

    def remove_vertice(self, u):
        incident_edges = [i for i, value in enumerate(self.grafo[u]) if value > 0]
        for edge_index in reversed(incident_edges):
            for i in range(self.num_v):
                self.grafo[i].pop(edge_index)
            self.num_a -= 1
        self.grafo.pop(u)
        self.num_v -= 1

    def remove_aresta(self, u, v):
        edge_index = None
        for i in range(self.num_a):
            if self.grafo[u][i] > 0 and self.grafo[v][i] > 0:
                edge_index = i
                break
        if edge_index is not None:
            for i in range(self.num_v):
                self.grafo[i].pop(edge_index)
            self.num_a -= 1

    def adjs(self, u):
        adjacents = []
        for i, value in enumerate(self.grafo[u]):
            if value > 0:
                for j in range(self.num_v):
                    if j != u and self.grafo[j][i] > 0:
                        adjacents.append(j)
        return adjacents

    def ha_aresta(self, u, v):
        for i in range(self.num_a):
            if self.grafo[u][i] > 0 and self.grafo[v][i] > 0:
                return True
        return False

    def grau(self, u):
        return sum(self.grafo[u])

    def tem_alguma_aresta(self, u):
        for i in range(self.num_a):
            if self.grafo[u][i] > 0:
                return True

    def eh_nulo(self):
        return self.num_v == 0
