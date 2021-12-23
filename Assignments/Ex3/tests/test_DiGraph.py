
import unittest

from Assignments.Ex3.src.DiGraph import DiGraph
from Assignments.Ex3.src.My_NodeData import My_NodeData


class test_DiGraph(unittest.TestCase):
    def creat_g(self)-> DiGraph:
        g = DiGraph()

        node = My_NodeData(1)
        node2 = My_NodeData(2)
        #  edege = My_EdgeData(node.getkey(), node2.getkey(), 10.2)
        tuple2 = (1, 1, 1)
        tuple3 = (2, 2, 2)
        g.add_node(node.getkey(), tuple2)
        g.add_node(node2.getkey(), tuple3)
        g.add_edge(node.getkey(), node2.getkey(), 10.2)
        return g

    def test_get_v(self): #need to do public function

        g=self.creat_g()
        self.assertTrue(g.get_v(1).getkey(),1)


    def test_v_size(self):
        g=self.creat_g()
        x = g.v_size()
        self.assertEqual(x,2)

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

        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
