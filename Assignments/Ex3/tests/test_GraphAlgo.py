from unittest import TestCase

from Assignments.Ex3.src.DiGraph import DiGraph
from Assignments.Ex3.src.GraphAlgo import GraphAlgo


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
        x =DiGraph()
        g=GraphAlgo(x)
        g.load_from_json("C:/Users/shaim/PycharmProjects/OOP/Assignments/Ex3/data/A0.json")
        print(g.get_graph().get_v(0).getkey())

    def test_save_to_json(self):
        x=DiGraph()
        g=GraphAlgo(x)
        g.load_from_json("C:/Users/shaim/PycharmProjects/OOP/Assignments/Ex3/data/A0.json")
        g.save_to_json("out.json")

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(1,7):
            g.add_node(i,(0,0,0))

        g.add_edge(1,6,14)

        g.add_edge(1, 3, 9)
        g.add_edge(2, 4, 15)
        g.add_edge(2, 3, 10)
        g.add_edge(1, 2, 7)
        g.add_edge(3, 4, 11)
        g.add_edge(6, 5, 9)
        g.add_edge(4,5,6)
        g.add_edge(3, 6, 2)
        g.add_edge(3, 4, 11)
        x = GraphAlgo(g)
        p = x.shortest_path(1,5)
        self.assertTrue(p[0],20)
        print(p[1])
        #self.assertTrue(p[1],(1,6))




    def test_plot_graph(self):
        self.fail()

    def test_get_graph(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        g = DiGraph()
        for i in range(1, 10):
            g.add_node(i, (0, 0, 0))

        g.add_edge(1, 2, 1)
        g.add_edge(2, 1, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 3, 1)
        g.add_edge(3, 5, 1)
        g.add_edge(5, 3, 1)
        g.add_edge(5, 6, 1)
        g.add_edge(6, 5, 1)
        g.add_edge(5, 7, 1)
        g.add_edge(7, 5, 1)
        g.add_edge(7, 8, 1)
        g.add_edge(8, 7, 1)
        g.add_edge(9, 8, 1)
        g.add_edge(8, 9, 1)
        x = GraphAlgo(g)

        p = x.centerPoint()
        print(p)
        self.assertTrue(p[0], 5)
        self.assertTrue(p[1], 3.0)

