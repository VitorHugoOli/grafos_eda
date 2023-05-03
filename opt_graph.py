import numpy as np
import networkx as nx
from itertools import chain, combinations

from grafo import Grafo


class OptimizedGrafo(Grafo):
    def __init__(self, num_v=0):
        super().__init__(num_v)
        self.num_v = num_v
        self.graph = nx.Graph()
        self.graph.add_nodes_from(range(num_v))

    def add_vertice(self, u):
        self.graph.add_node(u)
        self.num_v += 1

    def add_aresta(self, u, v):
        self.graph.add_edge(u, v)

    def remove_vertice(self, u):
        self.graph.remove_node(u)
        self.num_v -= 1

    def remove_aresta(self, u, v):
        self.graph.remove_edge(u, v)

    def adjs(self, u):
        return list(self.graph.neighbors(u))

    def ha_aresta(self, u, v):
        return self.graph.has_edge(u, v)

    def grau(self, u):
        return self.graph.degree(u)

    def tem_alguma_aresta(self, u):
        return bool(self.adjs(u))

    def eh_nulo(self):
        return self.num_v == 0

    def num_componentes_conexas_apos_remocao(self, vertices_to_remove):
        graph_copy = self.graph.copy()
        graph_copy.remove_nodes_from(vertices_to_remove)

        return nx.number_connected_components(graph_copy)

    def eh_hamiltoniano(self):
        V = set(self.graph.nodes())

        def todos_subconjuntos(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

        for S in todos_subconjuntos(V):
            if self.num_componentes_conexas_apos_remocao(S) > len(S):
                return False

        return True
