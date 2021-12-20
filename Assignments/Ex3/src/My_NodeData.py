from Assignments.Ex3.src.Geolocation import Geolocation
from Assignments.Ex3.src.NodeData import NodeData


class My_NodeData(NodeData, Geolocation):


    def __init__(self):
        self.setlocation(self)
        self.tag = 0

