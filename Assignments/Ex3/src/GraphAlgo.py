from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from My_NodeData import My_NodeData
from DiGraph import DiGraph
from collections import deque
from queue import Queue



class GraphAlgo(GraphAlgoInterface):

    def __init__(self,g:DiGraph):
        self.graph = g

    def get_graph(self) -> DiGraph:
        """
         This method returns the graph which the Graph_Algo works on.
        :return: directed weighted graph.
        """
        return self.graph


    def DFS(self, id1: int) -> None:
        graph = self.graph


        stack = deque()
        stack.append(id1)

        n =  graph.get_v(id1)
        n.setTag(1) #mark as visited

        while len(stack) != 0:
            curr = stack.pop()
            #running on edges on keys <src,<dest,weight>>
            #neighbor = graph.all_in_edges_of_node(curr):
            for neighbor in graph.all_in_edges_of_node(curr):
                if graph.get_v(neighbor).getTag()!=1:
                       graph.get_v(neighbor).setTag(1)
                       stack.append(neighbor)



    def isConnected(self)->bool:
        g= self.graph


        if g == None:
            return True
        if g.e_size() == 0 or g.v_size() == 1:#maby () needed
            return True
        if g.v_size() > g.e_size() + 1:
            return False
        all_nodes = g.get_all_v().keys() #self might be needed
        for v in all_nodes:
              #g = My_NodeData(iterate_node.__next__())
              self.DFS(v)

              all_nodes2 = g.get_all_v().values()
              for v in all_nodes2:

                  if v.getTag() != 1 :
                      return False

                  v.setTag(0)



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

