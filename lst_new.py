from grafo import Grafo


class GrafoLstAdjNew(Grafo):
    def __init__(self, num_v=0):
        super().__init__(num_v=num_v)
        self.grafo: dict[int, list[int]] = {i: [] for i in range(num_v)}

    def add_vertice(self):
        self.grafo[self.num_v] = []
        self.num_v += 1

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
        del self.grafo[u]
        for adj_list in self.grafo.values():
            if u in adj_list:
                adj_list.remove(u)
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
        return bool(self.grafo.get(u, []))

    def eh_nulo(self):
        return self.num_v == 0