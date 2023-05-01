from grafo import Grafo
from lst_adjacencia import GrafoLstAdj
from mtr_adjacencia import GrafoMtrAdj
from mtr_incidencia import GrafoMtrInc

path = 'graphs/graph_50.txt'
graph: GrafoMtrAdj = GrafoMtrAdj.read_graph(path)
# graph.display(filename='graph_mtr_adj')
print(graph.circuito_euleriano_new())

graph: GrafoMtrInc = GrafoMtrInc.read_graph(path)
# graph.display(filename='graph_mtr_inc')
print(graph.circuito_euleriano_new())

graph: GrafoLstAdj = GrafoLstAdj.read_graph(path)
# graph.display(filename='graph_lst_adj')
print(graph.circuito_euleriano_new())

# Create a complete graph
# graph = GrafoMtrAdj(5)
# graph.add_aresta(0, 1)
# graph.add_aresta(0, 2)
# graph.add_aresta(0, 3)
# graph.add_aresta(0, 4)
# graph.add_aresta(1, 2)
# graph.add_aresta(1, 3)
# graph.add_aresta(1, 4)
# graph.add_aresta(2, 3)
# graph.add_aresta(2, 4)
# graph.add_aresta(3, 4)
# graph.display()
# print(graph.circuito_euleriano_new())
