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

    def arestas(self):
        arestas = set()
        for u in range(self.num_v):
            for v in self.grafo[u]:
                if u < v:
                    arestas.add((u, v))
        return arestas

    def remove_vertice(self, u):
        for v in range(self.num_v):
            if u in self.grafo[v]:
                self.grafo[v].remove(u)
        self.grafo.pop(u)

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

    def eh_nulo(self):
        return self.num_v == 0
