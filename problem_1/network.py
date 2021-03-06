import numpy as np
import networkx as nx

'''
Network of traveling salesman problem (TSP)
Inspired by github : https://github.com/Boyu1997/mcts-travel-salesman
Create a random fully connected network as a random sample of TSP by using networkx
'''


class Network():

    def __init__(self, num_of_node, side_length):
        self.num_of_node = num_of_node
        self.side_length = side_length
        self.initialize_graph()


    def initialize_graph(self):

        # generate random node position
        nodes = np.random.randint(self.side_length, size=self.num_of_node*2)
        nodes = nodes.reshape(self.num_of_node, 2)
        self.positions = {key: tuple(node) for key, node in enumerate(nodes)}

        # setup the graph
        self.graph = nx.Graph()
        self.graph.add_nodes_from([i for i in range(self.num_of_node)])

        # setup edge and weight
        for i in range(self.num_of_node-1):
            d = nodes[i] - nodes[i+1:, :]
            weight = (d[:, 0]**2 + d[:, 1]**2)**0.5
            weighted_edges = [(i, i+j, weight[j-1]) for j in range(1, self.num_of_node-i)]
            self.graph.add_weighted_edges_from(weighted_edges)
