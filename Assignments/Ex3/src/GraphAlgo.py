import collections
import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface

from DiGraph import DiGraph
from collections import deque

import queue
from queue import PriorityQueue

from My_NodeData import My_NodeData


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

        graph=DiGraph()
        try:
            with open (file_name,"r") as f:
                my_list = json.load(f)
                for node in my_list["Nodes"]:
                    pos = node["pos"]
                    s=pos.split(',')
                    x=float(s[0])
                    y=float(s[1])
                    z=float(s[2])
                    p=(x,y ,z)
                    id = node["id"]
                    graph.add_node(node_id=id ,pos=tuple(p))
                for i in my_list["Edges"]:
                    Src = i["src"]
                    w=i["w"]
                    dest=i["dest"]
                    graph.add_edge(Src,dest,w)

            self.graph=graph
            return True

        except EOFError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
           with open(file_name , "w")as f:
               my_ans={}
               nodes=[]
               edeges=[]

               for node in self.graph.get_all_v().values():
                   nodes.append({"pos":node.getlocation(),"id": node.getkey()})

                   for edge , weith in self.graph.all_in_edges_of_node(node.getkey()).items():
                        edeges.append({"src":node.getkey() ,"wight":weith,"dest":edge})


               my_ans["Edges"]=edeges
               my_ans["Nodes"]=nodes

               json.dump(my_ans,indent=6 ,fp=f)


           return True

        except EOFError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        #returning path + distance
        g = self.graph
        first_res = 0
        pq = PriorityQueue()
        my_nodes = g.get_all_v().values()
       # print(my_nodes)
        #ntest = My_NodeData(1,(1,1,1))
        #ntest.setInfo("jungling")
        for node in my_nodes:
            node.setWeight(100000)
            node.setInfo("White")
            pq.put(node)

        g.get_v(id1).setWeight(0)

        while not pq.empty():
            #does get() is like pop()?
              n = pq.get()

              edges_of_n = g.all_in_edges_of_node(n.getkey()).items()
            #<src,<dest,weight>
            #running <dest,weight>
              for dest,weight in edges_of_n:
                  #getting the dest node
                  #edge = My_EdgeData(n.getkey,dest,weight)

                  n_next = g.get_v(dest)

                  if n_next.getInfo()!="red":
                     t = n.getWeight() +weight

                     if n_next.getWeight()>t:
                         n_next.setWeight(t)
                         n_next.prev = n.getkey()
                         pq.put(n_next)
                         #maby pq.remove(u) needed
                  n.setInfo("red")


        first_res = g.get_v(id2).key

            #now the path
        ans = []
        anse_helper = deque()
        curr = g.get_v(id2)
        ans.append(curr.getkey())

        anse_helper.appendleft(curr.getkey())
        
        while curr.getkey()!=id1:
            pred = curr.prev
            curr = g.get_v(pred)
            anse_helper.appendleft(curr.getkey())
            #ans.append(curr.getkey())
        ans = list(anse_helper)


        return  first_res,ans
























        pass

    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return self.graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

