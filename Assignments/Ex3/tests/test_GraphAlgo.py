from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):


    def test_is_connected(self):
        g = DiGraph()
        for i in range(4):
            g.add_node(i)

        g.add_edge(0,1,10)
        g.add_edge(0, 3,10)
        g.add_edge(1, 2,10)
        g.add_edge(2, 0,10)
        g.add_edge(3, 2,10)

        graph_in_algo = GraphAlgo(g)

        print(graph_in_algo.isConnected())

        g.remove_edge(2,0)

        print(graph_in_algo.isConnected())
        #self.assertTrue(graph_in_algo.isConnected(),True)



    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def test_get_graph(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()
