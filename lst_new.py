from grafo import Grafo, GrafoProrio


class GrafoLstAdjNew(Grafo):
    def __init__(self, num_v=0):
        super().__init__(num_v=num_v)
        self.grafo_shadow = None
        self.grafo: dict[int, list[int]] = {i: [] for i in range(num_v)}

    def add_vertice(self, u):
        self.grafo[u] = []
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

    def num_componentes_conexas_apos_remocao(self, vertices_to_remove):
        """
        Calcula o número de componentes conexas após a remoção de um conjunto de vértices.

        Parâmetros:
        G (Grafo): Um grafo representado usando a classe Grafo.
        vertices_to_remove (set): Um conjunto de vértices para remover do grafo G.

        Retorna:
        int: O número de componentes conexas após a remoção dos vértices.
        """
        # H: GrafoProrio = self.__copy__(self)

        # H = G − S
        visited = [False] * self.grafo_shadow.num_v
        num = self.grafo_shadow.num_v
        for v in vertices_to_remove:
            self.grafo_shadow.remove_vertice(v)
            visited[v] = True

        num_components = 0

        # ω(H)
        for v in range(num):
            if not visited[v]:
                num_components += 1
                self.grafo_shadow.bp(v, visited)

        for v in vertices_to_remove:
            self.grafo_shadow.add_vertice(v)

        for v in vertices_to_remove:
            for i in self.adjs(v):
                self.grafo_shadow.add_aresta(v, i)

        return num_components

    def eh_hamiltoniano(self):
        """
        Verifica se a condição necessária para um grafo ser Hamiltoniano é satisfeita.

        Retorna:
        bool: Retorna True se a condição for satisfeita, caso contrário retorna False.
        """
        self.grafo_shadow = self.__copy__(self)

        V = set(self.vertices())  # qualquer subconjunto próprio não vazio S ⊂ V

        for S in self.todos_subconjuntos(V):
            if self.num_componentes_conexas_apos_remocao(S) > len(S):  # vale a relação ω(G − S) ≤ |S|
                return False

        return True
