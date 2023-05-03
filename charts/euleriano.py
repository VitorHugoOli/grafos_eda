import matplotlib.pyplot as plt
from analysis import Analysis as analysis
from lst_adjacencia import GrafoLstAdj
from mtr_adjacencia import GrafoMtrAdj
from mtr_incidencia import GrafoMtrInc


def count_operations_and_edges(graph_size):
    path = f'../graphs/graph_{graph_size}.txt'

    graph: GrafoMtrAdj = GrafoMtrAdj.read_graph(path)
    edges = len(graph.arestas())
    graph.circuito_euleriano()
    adj_operations = analysis.COUNTER
    analysis.COUNTER = 0

    graph: GrafoMtrInc = GrafoMtrInc.read_graph(path)
    graph.circuito_euleriano()
    inc_operations = analysis.COUNTER
    analysis.COUNTER = 0

    graph: GrafoLstAdj = GrafoLstAdj.read_graph(path)
    graph.circuito_euleriano()
    lst_operations = analysis.COUNTER
    analysis.COUNTER = 0

    return adj_operations, inc_operations, lst_operations, edges


graph_sizes = list(range(5, 51, 5))
adj_counts = []
inc_counts = []
lst_counts = []
edges_counts = []

for size in graph_sizes:
    adj_operations, inc_operations, lst_operations, edges = count_operations_and_edges(size)
    adj_counts.append(adj_operations)
    inc_counts.append(inc_operations)
    lst_counts.append(lst_operations)
    edges_counts.append(edges)

plt.xlabel('Tamanho do Grafo')
plt.ylabel('Quantidade de Operações')
plt.title('Comparação das Operações por Estrutura de Dados')
plt.plot(graph_sizes, adj_counts, label='Matriz de Adjacências')
plt.plot(graph_sizes, [edges * size for size, edges in zip(graph_sizes, edges_counts)], label='O(A * V)', linestyle='--')
x_labels = [f'({size},{edges})' for size, edges in zip(graph_sizes, edges_counts)]
plt.xticks(graph_sizes, x_labels, rotation=45)
plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig("chart_adj.png")
plt.show()

plt.xlabel('Tamanho do Grafo')
plt.ylabel('Quantidade de Operações')
plt.title('Comparação das Operações por Estrutura de Dados')
plt.plot(graph_sizes, inc_counts, label='Matriz de Incidência')
plt.plot(graph_sizes, [(edges ** 2) * (size ** 2) for size, edges in zip(graph_sizes, edges_counts)],
         label='O(A^2 * V^2)', linestyle='--')
x_labels = [f'({size},{edges})' for size, edges in zip(graph_sizes, edges_counts)]
plt.xticks(graph_sizes, x_labels, rotation=45)
plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig("chart_inc.png")
plt.show()

plt.xlabel('Tamanho do Grafo')
plt.ylabel('Quantidade de Operações')
plt.title('Comparação das Operações por Estrutura de Dados')
plt.plot(graph_sizes, lst_counts, label='Lista de Adjacências')
plt.plot(graph_sizes, [size * edges for size, edges in zip(graph_sizes, edges_counts)], label='O(V * A)',
         linestyle='--')
x_labels = [f'({size},{edges})' for size, edges in zip(graph_sizes, edges_counts)]
plt.xticks(graph_sizes, x_labels, rotation=45)
plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig("chart_lst.png")
plt.show()