from collections import deque
from copy import copy, deepcopy
from itertools import chain, combinations

import graphviz


class GrafoBase:
    def __init__(self, num_v=0):
        # Será usada para inicializar a estrutura de dados e inicializar a variável num_v(número de vértices)
        self.num_v = num_v
        pass

    def add_vertice(self):
        # Adiciona um vértice ao grafo
        pass

    def add_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        pass

    def arestas(self) -> list[tuple]:
        # Retorna uma lista de tuplas (u, v) que representam as arestas do grafo
        pass

    def vertices(self) -> list:
        pass

    def remove_aresta(self, u, v):
        # Remove a aresta entre os vértices u e v
        pass

    def remove_vertice(self, u):
        # Remove o vértice u do grafo
        pass

    def adjs(self, u) -> list[int]:
        # Retorna uma lista com os vértices adjacentes a u
        pass

    def ha_aresta(self, u, v):
        # O vértice u tem uma aresta com o vértice v?
        pass

    def grau(self, u) -> int:
        # O grau de um vértice é o número de arestas que incidem nele
        pass

    def tem_alguma_aresta(self, u):
        # O vértice tem alguma aresta?
        pass


class GrafoDisplayMixin(GrafoBase):

    def __str__(self):
        # Create a string representation of the graph
        graph_str = "Vertices:\n"
        for vertex in self.vertices():
            graph_str += f"{vertex}\n"

        graph_str += "\nArestas:\n"
        for u, v in self.arestas():
            graph_str += f"({u}, {v})\n"

        return graph_str

    def display(self, filename='graph'):
        folder = 'graphiz'
        # Create a Graphviz object to represent the graph
        dot = graphviz.Graph()

        # Graph settings
        dot.attr(overlap='false', splines='true', pad='0.5')

        # Node settings
        dot.attr('node', shape='circle', style='filled', fillcolor='lightblue', fontname='Helvetica', fontsize='14')

        # Edge settings
        dot.attr('edge', color='black', fontname='Helvetica', fontsize='12')

        # Add vertices to the graph
        for vertex in self.vertices():
            dot.node(str(vertex))

        # Add edges to the graph
        for u, v in self.arestas():
            dot.edge(str(u), str(v), label=f"{u}-{v}")

        # Display the graph
        dot.view(filename=folder + '/' + filename)


class GrafoReadFileMixin(GrafoBase):
    @classmethod
    def read_graph(cls, file_name):
        with open(file_name, 'r') as f:
            # get the len of lines in file
            lines = len(f.readlines())
            graph_instance = cls(num_v=lines)
            visited = [False] * lines
            f.seek(0)
            for i in range(lines):
                visited[i] = True
                line = f.readline().replace('\n', '').split(',')
                for j in line:
                    if not visited[int(j)]:
                        graph_instance.add_aresta(i, int(j))
        return graph_instance


class GrafoProrio(GrafoDisplayMixin, GrafoReadFileMixin):
    def __init__(self, num_v=0):
        super().__init__(num_v=num_v)

    def vertices(self):
        return [v for v in range(self.num_v)]

    def bp(self, v, visited):
        visited[v] = True
        for i in self.adjs(v):
            if not visited[i]:
                self.bp(i, visited)

    def eh_conectado(self):
        visited = [False] * self.num_v
        i = 0

        # Achando um vértice com grau maior que 0
        for i in range(self.num_v):
            if self.tem_alguma_aresta(i):
                break

        # Se o grau de todos os vértices for 0, o grafo é nulo
        if i == self.num_v - 1:
            return False

        self.bp(i, visited)

        for i in range(self.num_v):
            if not visited[i] and len(self.adjs(i)) > 0:
                return False
        return True

    @classmethod
    def __copy__(cls, self):
        new_graph = cls(num_v=self.num_v)
        # for u, v in self.arestas():
        #     new_graph.add_aresta(u, v)
        new_graph.grafo = deepcopy(self.grafo)
        return new_graph


class GrafoEulerianoPathMixin(GrafoProrio):
    def eh_euleriano(self):
        if not self.eh_conectado():
            return False

        odd = 0

        for i in range(self.num_v):
            if self.grau(i) % 2 != 0:
                odd += 1

        if odd > 2:
            return False
        return True

    def circuito_euleriano(self):
        circuit = []

        if not self.eh_euleriano():
            return circuit

        stack: deque = deque()
        stack.append(0)
        count = 0

        while len(stack) > 0:
            count += 1

            current_vertex = stack[-1]

            adjs = self.adjs(current_vertex)

            if len(adjs) > 0:  # Grau do vértice é maior que 0
                neighbor = adjs[0]
                stack.append(neighbor)
                self.remove_aresta(current_vertex, neighbor)
            else:
                circuit.append(stack.pop())

        circuit.reverse()
        return circuit


class GrafoHamiltonianoMixin(GrafoProrio):
    @staticmethod
    def todos_subconjuntos(s):
        """
        Gera todos os subconjuntos próprios não vazios de S.

        Parâmetros:
        S (set): Um conjunto de vértices.

        Retorna:
        list: uma lista contendo todos os subconjuntos próprios não vazios de S.
        """
        return list(chain.from_iterable(combinations(s, r) for r in range(1, len(s))))

    def num_componentes_conexas_apos_remocao(self, vertices_to_remove):
        """
        Calcula o número de componentes conexas após a remoção de um conjunto de vértices.

        Parâmetros:
        G (Grafo): Um grafo representado usando a classe Grafo.
        vertices_to_remove (set): Um conjunto de vértices para remover do grafo G.

        Retorna:
        int: O número de componentes conexas após a remoção dos vértices.
        """
        H: GrafoProrio = self.__copy__(self)

        # H = G − S
        count = 0
        for v in vertices_to_remove:
            i = v - count
            H.remove_vertice(i)
            count += 1

        visited = [False] * H.num_v
        num_components = 0

        # ω(H)
        for v in range(H.num_v):
            if not visited[v]:
                num_components += 1
                H.bp(v, visited)

        return num_components

    def eh_hamiltoniano(self):
        """
        Verifica se a condição necessária para um grafo ser Hamiltoniano é satisfeita.

        Retorna:
        bool: Retorna True se a condição for satisfeita, caso contrário retorna False.
        """

        V = set(self.vertices())  # qualquer subconjunto próprio não vazio S ⊂ V

        for S in self.todos_subconjuntos(V):
            if self.num_componentes_conexas_apos_remocao(S) > len(S):  # vale a relação ω(G − S) ≤ |S|
                return False

        return True


class Grafo(GrafoEulerianoPathMixin, GrafoHamiltonianoMixin):
    pass
