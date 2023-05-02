from lst_adjacencia import GrafoLstAdj
from lst_new import GrafoLstAdjNew
from mtr_adjacencia import GrafoMtrAdj
from mtr_incidencia import GrafoMtrInc

path = 'graphs/graph_5.txt'
# graph: GrafoMtrAdj = GrafoMtrAdj.read_graph(path)
# graph.display(filename='graph_mtr_adj')
# print(graph.circuito_euleriano())
# print(graph.eh_hamiltoniano())

# graph: GrafoMtrInc = GrafoMtrInc.read_graph(path)
# graph.display(filename='graph_mtr_inc')
# print(graph.circuito_euleriano())
# print(graph.eh_hamiltoniano())

graph: GrafoLstAdj = GrafoLstAdj.read_graph(path)
graph.add_aresta(3, 4)
graph.display(filename='graph_lst_adj')
# print(graph.circuito_euleriano())
print(graph.eh_hamiltoniano())

# Create a graph that is hamiltonian
graph: GrafoLstAdj = GrafoLstAdj(num_v=5)
graph.add_aresta(0, 1)
graph.add_aresta(1, 2)
graph.add_aresta(2, 3)
graph.add_aresta(3, 4)
graph.add_aresta(4, 0)
graph.add_aresta(0, 2)
graph.add_aresta(2, 4)
graph.add_aresta(4, 1)
graph.add_aresta(1, 3)
graph.add_aresta(3, 0)
# graph.display(filename='graph_test')
# print(graph.circuito_euleriano())
# print(graph.eh_hamiltoniano())
