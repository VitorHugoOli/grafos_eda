import matplotlib.pyplot as plt
from analysis import Analysis as analysis
from lst_adjacencia import GrafoLstAdj
from mtr_adjacencia import GrafoMtrAdj
from mtr_incidencia import GrafoMtrInc


def count_operations_and_edges(graph_size):
    path = f'../graphs/graph_{graph_size}.txt'

    graph: GrafoLstAdj = GrafoLstAdj.read_graph(path)
    edges = len(graph.arestas())
    graph.eh_hamiltoniano()
    lst_operations = analysis.COUNTER
    analysis.COUNTER = 0

    return lst_operations, edges


graph_sizes = list(range(3, 15, 3))
adj_counts = []
inc_counts = []
lst_counts = []
edges_counts = []

for size in graph_sizes:
    lst_operations, edges = count_operations_and_edges(size)
    lst_counts.append(lst_operations)
    edges_counts.append(edges)

plt.xlabel('Tamanho do Grafo')
plt.ylabel('Quantidade de Operações')
plt.title('Comparação das Operações Basicas por entrada')
plt.plot(graph_sizes, lst_counts, label='Lista de Adjacências')
# O(2V ∗ (V ∗ S + 2 ∗ V + A))
plt.plot(graph_sizes, [(2 ** size) * (size * size + 2 * size + edges) for size, edges in zip(graph_sizes, edges_counts)],
         label='O(2V ∗ (V ∗ S + 2 ∗ V + A))',
         linestyle='--')
x_labels = [f'({size},{edges})' for size, edges in zip(graph_sizes, edges_counts)]
plt.xticks(graph_sizes, x_labels, rotation=45)
plt.legend()
plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig("chart_hamilton_lst.png")
plt.show()
