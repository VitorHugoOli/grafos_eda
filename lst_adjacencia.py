from analysis import Analysis as analysis
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

    def arestas(self):  # Usado para o copy
        arestas = set()
        for u in range(self.num_v):
            for v in self.grafo[u]:
                if u < v:
                    arestas.add((u, v))
        return arestas

    def remove_vertice(self, u):
        if len(self.grafo[u]) == 0:
            return

        # Remove o vertice u das listas de adjacencia dos outros vertices
        for v in range(self.num_v):
            for i, w in enumerate(self.grafo[v]):
                analysis.COUNTER += 1
                if w == u:
                    analysis.COUNTER += self.grau(v)
                    self.grafo[v].pop(i)
                if i >= len(self.grafo[v]):
                    break
                w = self.grafo[v][i]
                if w > u:
                    self.grafo[v][i] -= 1

        self.grafo.pop(u)
        self.num_v -= 1

    def remove_aresta(self, u, v):
        analysis.COUNTER += self.grau(u) + self.grau(v)
        self.grafo[u].remove(v)
        self.grafo[v].remove(u)

    def adjs(self, u):
        analysis.COUNTER += 1
        return self.grafo[u]

    def ha_aresta(self, u, v):
        analysis.COUNTER += self.grau(u)
        return v in self.grafo[u]

    def grau(self, u):
        analysis.COUNTER += 1
        return len(self.grafo[u])

    def tem_alguma_aresta(self, u):
        analysis.COUNTER += 1
        return len(self.grafo[u]) > 0
