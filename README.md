# Ex3 OOP
welcome to the fourth assignment in OOP course .
at this task we build weighted and directed graphs ,so we 
convert our EX2 at java to python and we compared the result.

# classes 
My_Nodedata
  this class implements NodeData interface represent node at graph
  that have id=name_of_node and location=(0,0,0) 
  
 My_EdgeData
 this class implements EdgeData interface represent Edge at graph
 that have source destination and weight
 
 DiGraph
  this class implements Graphinterface interface represent a weighted
  and directed graph.
  | Name of function | Description |
  |------------------|-------------|
  | init(self)       | constractor function|
  | get_v(self,key)  | returns the My_NodeData ig id equals key |
  | v_size(self)     | returns the size of the Nodes in the graph |
  | get_all_v(self)  | returns all the nodes in the graph by dict|
  | all_in_edges_of_node(self,id1: int)||return a dictionary of all the nodes connected to node_id|
  |all_out_edges_of_node(self, id1: int)| return a dictionary of all the nodes connected from node_id|
  |get_mc(self) | Returns the current version of this graph|
  |add_edge(self, id1: int, id2: int, weight: float) | Adds an edge to the graph ,return: True if the edge was added successfully, False o.w.|
  | add_node(self, node_id: int, pos: tuple = None) |   Adds a node to the graph.return: True if the node was added successfully, False o.w.|
  |remove_node(self, node_id: int)| Removes a node from the graph.return: True if the edge was removed successfully, False o.w.|
  |remove_edge(self, node_id1: int, node_id2: int)|Removes an edge from the graph.return: True if the edge was removed successfully, False o.w.|
  
  GraphAlgo
   this class implements GraphAlgointerface interface 
  
 
