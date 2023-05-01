from collections import deque

import graphviz


class GrafoDisplayMixin:
    def vertices(self) -> list:
        pass

    def arestas(self) -> list:
        pass

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


class Grafo(GrafoDisplayMixin):
    def __init__(self, num_v=0):
        self.num_v = num_v
        pass

    def add_vertice(self):
        pass

    def add_aresta(self, u, v):
        pass

    def arestas(self) -> list[tuple]:
        pass

    def remove_aresta(self, u, v):
        pass

    def remove_vertice(self, u):
        pass

    def adjs(self, u) -> list[int]:
        pass

    def ha_aresta(self, u, v):
        pass

    def grau(self, u) -> int:
        pass

    def tem_alguma_aresta(self, u):
        pass

    def eh_nulo(self):
        pass

    '''
    Métodos própios
    '''

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

    def vertices(self):
        return [v for v in range(self.num_v)]

    def eh_trivial(self):
        return self.num_v == 1

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

        visited = [False] * self.num_v
        visited[0] = True
        stack: list = [0]
        current_vertex = 0
        count = 0

        arestas = self.arestas()

        while len(stack) > 0:
            count += 1

            adjs = self.adjs(current_vertex)

            if len(adjs) > 0:
                neighbor = adjs[-1]
                self.remove_aresta(current_vertex, neighbor)
                current_vertex = neighbor
            else:
                circuit.append(current_vertex)
                current_vertex = stack.pop()

            if not visited[current_vertex]:
                visited[current_vertex] = True
                stack.append(current_vertex)

        print(f"arestas: {len(arestas)}, count: {count}")
        circuit.reverse()
        return circuit

    def circuito_euleriano_new(self):
        circuit = []

        if not self.eh_euleriano():
            return circuit

        stack: deque = deque()
        stack.append(0)
        count = 0

        arestas = self.arestas()

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

        print(f"arestas: {len(arestas)}, vertices: {self.num_v}, count: {len(arestas) + self.num_v} - {count}")
        circuit.reverse()
        return circuit
