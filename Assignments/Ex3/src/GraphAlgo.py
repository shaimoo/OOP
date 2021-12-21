from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from My_NodeData import My_NodeData




class GraphAlgo(GraphAlgoInterface):

    def DFS(param):

        pass


    def __init__(self,o=DiGraph):

        if DiGraph==None :
           self.graph = DiGraph()
        else:
            self.graph = o

    def isConnected(self)->bool:
        if self.graph == None:
            return True
        if self.graph.e_size() == 0 or self.graph.v_size() == 1:#maby () needed
            return True
        if self.graph.v_size() > self.graph.e_size() + 1:
            return False
        iterate_node = self.graph.get_all_v().__iter__()
        while iterate_node:
              g = My_NodeData(iterate_node.__next__())
              self.DFS(self, g.getkey())
              iterate_node2 = self.graph.get_all_v().__iter__()
              while iterate_node2:
                  g  = iterate_node2.__next__()
                  if g.getTag!=1 :
                      return False
              g.setTag(0)

        return True














    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return super().get_graph()

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

