from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from My_NodeData import My_NodeData
from DiGraph import DiGraph




class GraphAlgo(GraphAlgoInterface):

    def __init__(self,g:DiGraph):
        self.graph = g


"""private void DFS(int key) {
        Stack<NodeData> s = new Stack<NodeData>();
        NodeData t = this.g.getNode(key);
        s.push(t);
        t.setTag(1); //each and evrynode if visited
        while (!s.isEmpty()) {
            t = s.pop();
            Iterator<EdgeData> e = this.g.edgeIter(t.getKey());
            while (e.hasNext()) {
                EdgeData ed = e.next();
                //checking on neiighobs
                if (this.g.getNode(ed.getDest()).getTag() != 1) {//check if  visited
                    this.g.getNode(ed.getDest()).setTag(1);//set as visited
                    s.push(this.g.getNode(ed.getDest()));
                }
            }
        }
    }


    @Override
    public boolean isConnected() {
        /**dfs for each node**/
       if (this.g == null)
           return true;
       if (this.g.edgeSize() == 0 || this.g.nodeSize() == 1)
           return true;
       if (this.g.nodeSize() > this.g.edgeSize() + 1)
           return false;
       Iterator<NodeData> e =
"""

    def DFS(self,param:int):
       stack = []
       t=self.graph.get_v(param)
       stack.append(t)
       t.setTag(1)
       while stack.__sizeof__()>0:
            t=stack.pop()
            Iterator =self.graph.all_in_edges_of_node(t.key).__iter__()
            while not Iterator == None:
                ed =Iterator.__next__()
                if self.graph.get_v(ed.getDest().getTag()) != 1 :
                    self.graph.get_v(ed.getDest().setTag(1))
                stack.append(self.graph.get_v(ed.getDest()))



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
              self.DFS(g.getkey())
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

