from unittest import TestCase

from Assignments.Ex3.src.DiGraph import DiGraph
from Assignments.Ex3.src.My_EdgeData import My_EdgeData
from Assignments.Ex3.src.My_Geolocation import My_Geolocarion
from Assignments.Ex3.src.My_NodeData import My_NodeData


class TestDiGraph(TestCase):
    g=DiGraph()
    location= My_Geolocarion(1,1,1)
    location2 = My_Geolocarion(2,2,2)
    node = My_NodeData(1,location)
    node2 = My_NodeData(2,location2)
    edege = My_EdgeData(node.getkey(),node2.getkey(),10.2)
    tuple = (1,1,1)
    tuple2 = (2,2,2)
    g.add_node(node.getkey(),tuple)
    g.add_node(node2.getkey(),tuple2)
    g.add_edge(node.getkey(),node2.getkey(),10.2)

    def test_get_v(self):

        self.assertTrue(self.node.getkey(),self.g.get_v(self.node.getkey()).getkey())
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
