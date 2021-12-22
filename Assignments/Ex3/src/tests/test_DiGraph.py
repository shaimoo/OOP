from unittest import TestCase

from src.DiGraph import DiGraph
from src.My_EdgeData import My_EdgeData

from src.My_NodeData import My_NodeData


class TestDiGraph(TestCase):


    def test_get_v(self): #need to do public function
        g = DiGraph()

        node = My_NodeData(1)
        node2 = My_NodeData(2)
        edege = My_EdgeData(node.getkey(), node2.getkey(), 10.2)
        tuple2 = (1, 1, 1)
        tuple3 = (2, 2, 2)
        g.add_node(node.getkey(), tuple2)
        g.add_node(node2.getkey(), tuple3)
        g.add_edge(node.getkey(), node2.getkey(), 10.2)

        self.assertTrue(node.getkey(),g.get_v(node.getkey()).getkey())
        self.fail()

    def test_v_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.g.get
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
