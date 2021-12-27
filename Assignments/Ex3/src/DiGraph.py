from Assignments.Ex3.src.GraphInterface import GraphInterface
from Assignments.Ex3.src.My_NodeData import My_NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.EdgeSize = 0
        self.nodes = {}
        self.edges_in = {}
        self.edges_out= {}
        self.MC = 0

    def get_v(self, key) -> My_NodeData:
        return self.nodes[key]

    def v_size(self) -> int:
        return len(self.nodes)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return dict(self.edges_in[id1])

    def all_out_edges_of_node(self, id1: int) -> dict:
        return dict(self.edges_in[id1])

    def e_size(self) -> int:

        return self.EdgeSize

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if self.edges_in[id1].get(id2):
            return False

        if not self.nodes[id1] or not self.nodes[id2]:
            return False
        else:

            self.edges_in[id1][id2] = weight

            self.MC += 1
            self.EdgeSize += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id):
            return False
        else:
            #arr[k] = 5
            self.nodes[node_id] =My_NodeData(node_id,pos)
            self.edges_in[node_id] = {}
            self.MC += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if not self.nodes[node_id]:
            return False

        else:
            del self.nodes[node_id]
            if self.edges_in[node_id]:
                self.EdgeSize -= len(self.edges_in[node_id])
                del self.edges_in[node_id]
                self.MC+=1



        return True

    def get_all_e_in(self) -> dict:
        return self.edges_in

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.nodes[node_id1] and self.nodes[node_id2] and node_id2 in self.edges_in[node_id1] :
            self.EdgeSize-=1
            self.MC += 1
            self.edges_in.get(node_id1).pop(node_id2)
            return True
        return False
