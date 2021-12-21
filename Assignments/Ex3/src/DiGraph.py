from NodeData import NodeData
from Geolocation import Geolocation
from EdgeData import EdgeData
from  My_EdgeData import My_EdgeData
from My_Geolocation import My_Geolocarion

from GraphInterface import GraphInterface

class DiGraph(GraphInterface):

     def __init__(self):

         self.vertesis = {}
         self.edges_in = {}
         self.edges_out = {}
         self.MC = 0

    def v_size(self) -> int:

        return self.v

        pass

    def get_all_v(self) -> dict:
        return super().get_all_v()

    def all_in_edges_of_node(self, id1: int) -> dict:
        return super().all_in_edges_of_node(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return super().all_out_edges_of_node(id1)

    def e_size(self) -> int:

        return (self.edges_in+self.edges_out)/2

    def get_mc(self) -> int:
        pass self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if self.edges_in[id1] :


            return False

        if not  self.vertesis_in[id1] or not self.vertesis[id2]:

            return False


        else:
            edge = My_EdgeData(id1,id2,weight)
            edge2 = My_EdgeData(id2,id1,weight)
            self.edges_in.append(id1,edge)
            self.edges_out.append(id2,edge2)
            self.MC+=1
            return True


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.vertesis[node_id]:
         return False
        else:
         self.vertesis.append(node_id,My_Geolocarion(pos))
         self.MC+=1
         return True



    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass