
import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


# Driver code
G = GraphVisualization()

G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 3)
G.addEdge(1, 4)
G.addEdge(2, 5)
G.addEdge(2, 6)
G.addEdge(3, 7)
G.addEdge(3, 8)
G.addEdge(4, 9)
G.addEdge(4, 10)
G.addEdge(5, 11)
G.addEdge(5, 12)
G.addEdge(6, 13)
G.addEdge(6, 14)

G.visualize()


