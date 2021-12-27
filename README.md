# Ex3 OOP
welcome to the fourth assignment in OOP course .
at this task we build weighted and directed graphs ,so we 
convert our EX2 at java to python and we compared the result.

## classes 
-My_Nodedata
  this class implements NodeData interface represent node at graph
  that have id=name_of_node and location=(0,0,0) 
  
 
- DiGraph
  this class implements Graphinterface interface represent a weighted
  and directed graph.
  | Name of function | Description |
  |------------------|-------------|
  | init(self)       | constractor function|
  | get_v(self,key)  | returns the My_NodeData ig id equals key |
  | v_size(self)     | returns the size of the Nodes in the graph |
  | get_all_v(self)  | returns all the nodes in the graph by dict|
  | all_in_edges_of_node(self,id1: int)|return a dictionary of all the nodes connected to node_id|
  |all_out_edges_of_node(self, id1: int)| return a dictionary of all the nodes connected from node_id|
  |get_mc(self) | Returns the current version of this graph|
  |add_edge(self, id1: int, id2: int, weight: float) | Adds an edge to the graph ,return: True if the edge was added successfully, False o.w.|
  | add_node(self, node_id: int, pos: tuple = None) |   Adds a node to the graph.return: True if the node was added successfully, False o.w.|
  |remove_node(self, node_id: int)| Removes a node from the graph.return: True if the edge was removed successfully, False o.w.|
  |remove_edge(self, node_id1: int, node_id2: int)|Removes an edge from the graph.return: True if the edge was removed successfully, False o.w.|
  
- GraphAlgo
  this class implements GraphAlgointerface interface 
 | Name of function | Description |
 |------------------|-------------|
 | get_graph(self)       | :return: the directed graph on which the algorithm works on.|
 |  DFS(self, id1: int)     | implementation of dfc algorithm do it about all the node.| 
 |  isConnected(self) | :return: if the graph is conect or no |
 | load_from_json(self, file_name: str)      | returns True if the loading was successful, False o.w.|
 |  save_to_json(self, file_name: str)      |  returns True if the loading was successful, False o.w.|
 |   shortest_path(self, id1: int, id2: int)       | using dijkstra algorithm . returns The distance of the path, a list of the nodes ids that the path goes through|
 | TSP(self, node_lst: List[int])     |  A list of the nodes id's in the path, and the overall distance|
 |  centerPoint(self)    | :return: The nodes id, min-maximum distance|
 |  plot_graph(self)     |  If the nodes have a position, the nodes will be placed there.Otherwise, they will be placed in a random but elegant manner.return: None|
        

  ##how to download 
- To download the task from GitHub, you should navigate to the top level of the project (SDN in this case) and then a green "Code" download button will be visible on the right.
   Choose the Download ZIP option from the Code pull-down menu. That ZIP file will contain the entire repository content.
  ##how to use 
- After you download the task at zip you need to extract  the zip file , then you need 
  to open pycharm and run the main file .....

