from analysis import Analysis as analysis
from lst_adjacencia import GrafoLstAdj
from lst_new import GrafoLstAdjNew
from mtr_adjacencia import GrafoMtrAdj
from mtr_incidencia import GrafoMtrInc
from opt_graph import OptimizedGrafo

# path = 'graphs/graph_5.txt'
#
# graph: GrafoMtrAdj = GrafoMtrAdj.read_graph(path)
# graph.eh_hamiltoniano()
# print("Contagem da operação: ", analysis.COUNTER)
# analysis.COUNTER = 0
#
# graph: GrafoMtrInc = GrafoMtrInc.read_graph(path)
# graph.circuito_euleriano()
# print("Contagem da operação: ", analysis.COUNTER)
# analysis.COUNTER = 0
#
# graph: GrafoLstAdj = GrafoLstAdj.read_graph(path)
# graph.circuito_euleriano()
# print("Contagem da operação: ", analysis.COUNTER)
# print(graph.eh_hamiltoniano())

# graph: OptimizedGrafo = OptimizedGrafo.read_graph(path)
# graph.display(filename='graph_lst_adj_new')
# print(graph.circuito_euleriano())
# print(graph.eh_hamiltoniano())

# Create a graph that is hamiltonian
# graph: GrafoLstAdj = GrafoLstAdj(num_v=5)
# graph.add_aresta(0, 1)
# graph.add_aresta(1, 2)
# graph.add_aresta(2, 3)
# graph.add_aresta(3, 4)
# graph.add_aresta(4, 0)
# graph.add_aresta(0, 2)
# graph.add_aresta(2, 4)
# graph.add_aresta(4, 1)
# graph.add_aresta(1, 3)
# graph.add_aresta(3, 0)
# graph.display(filename='graph_test')
# print(graph.circuito_euleriano())
# print(graph.eh_hamiltoniano())


# graph: GrafoMtrInc = GrafoMtrInc(num_v=5)
# graph.add_aresta(0, 1)
# graph.add_aresta(0, 2)
# graph.add_aresta(1, 2)
#
# graph.add_aresta(0, 3)
# graph.add_aresta(1, 3)
# graph.add_aresta(2, 3)
#
# graph.add_aresta(0, 4)
# graph.add_aresta(1, 4)
# graph.add_aresta(2, 4)
# graph.add_aresta(3, 4)
#
# # graph.display(filename='graph_test')
# print((graph.num_v-1) * graph.num_v * (graph.num_v))
# visited = [False] * graph.num_v
# graph.bp(2, visited)
#
# print(Analysis.COUNTER)




# plt.xlabel('Tamanho do Grafo')
# plt.ylabel('Quantidade de Operações')
# plt.title('Comparação das Operações por Estrutura de Dados')
# plt.legend()
# plt.show()
