
from My_NodeData import My_NodeData
from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.EdgeSize = 0
        self.vertesis = {}
        self.edges_in = {}
        self.edges_out= {}
        self.MC = 0

    def get_v(self, key) -> My_NodeData:
        return self.vertesis[key]

    def v_size(self) -> int:
        return len(self.vertesis)

    def get_all_v(self) -> dict:
        return self.vertesis

    def all_in_edges_of_node(self, id1: int) -> dict:
        return dict(self.edges_in[id1])

    def all_out_edges_of_node(self, id1: int) -> dict:
        return dict(self.edges_out[id1])

    def e_size(self) -> int:

        return self.EdgeSize

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if self.edges_in[id1]:
            return False

        if not self.vertesis[id1] or not self.vertesis[id2]:
            return False
        else:

            self.edges_in[id1][id2] = weight
  #          self.edges_out[id2][id1] = weight
            self.MC += 1
            self.EdgeSize += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.vertesis.get(node_id):
            return False
        else:
            #arr[k] = 5
            self.vertesis[node_id] =My_NodeData(pos)
            self.edges_in[node_id] = {}
            self.MC += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if not self.vertesis[node_id]:
            return False

        else:
            del self.vertesis[node_id]
            if self.edges_in[node_id]:
                del self.edges_in[node_id]
            if self.edges_out[node_id]:
                self.EdgeSize -= len(self.edges_out[node_id])
                del self.edges_out[node_id]

        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.edges_in[node_id1][node_id2]:
            del self.edges_in[node_id1][node_id2]
            return True
        return False
