import switch as switch

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

def check():
    """
    Graph: |V|=4 , |E|=5
    {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    (2.8, [0, 1, 3])
    (inf, [])
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    (7, 6.806805834715163)
    ([1,3,4,2],3.5)
    """
    check0()
    check1()
    check2()
    check3()

def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print("check0")
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "C:/Users/shaim/PycharmProjects/OOP/Assignments/Ex3/data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print("check1")
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    print(g_algo.centerPoint())
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = 'C:/Users/shaim/PycharmProjects/OOP/Assignments/Ex3/data/A5.json'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    print("check2")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.TSP([1, 2, 3]))
    g_algo.plot_graph()


def check3():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g = DiGraph()  # creates an empty directed graph
    for n in range(5):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(1, 3, 1.9)
    g.add_edge(2, 3, 1.1)
    g.add_edge(3, 4, 2.1)
    g.add_edge(4, 2, .5)
    g_algo = GraphAlgo(g)
    print(g_algo.centerPoint())
    print(g_algo.TSP([1, 2, 4]))
    g_algo.plot_graph()


if __name__ == '__main__':
    check()

    x=input("hello you have few options  \n* click -1 to exit  \n* for load file anter  0 and then anter the full path \n* for save changes anter  1 and the namefile  "
          "\n* for the shorters path anter  2  then source and dest node \n* for build Empty graph you need to click 3 and anter node by node with space "
         "\n* for add edege click 4 and anter source dest and weith \n* for TSP anter 5 and the list \n* for center node anter 6"
          "\n* for remove node anter 7 and the node id \n* for for remove add anter 8 and the src and dest "
          "\n* for show the graph anter 9 " )
    g=GraphAlgo()
    while x[0] != -1 :
        if x[0] == 0 :
            g.load_from_json(x[1])
        if x[0] == 1:
            g.save_to_json(x[1])
        if x[0] == 2:
            print(str(g.shortest_path(int(x[1]),int(x[2]))))
        if x[0]== 3:
            g = GraphAlgo()
            for node in range(1,len(x)+1):
                g.graph.add_edge(node)
        if x[0] == 4:
            g.graph.add_edge(x[1],x[2],x[3])
        if x[0] == 5:
            mylist=[]
            for node in range(1, len(x) + 1):
                mylist.append(node)
            print(str(g.TSP(mylist)))

        if x[0] == 6:
            print(str(g.centerPoint()))
        if x[0] == 7:
            g.graph.remove_node(x[1])
        if x[0] == 8:
            g.graph.remove_edge(x[1],x[2])
        if x[0] == 9 :
            g.plot_graph()