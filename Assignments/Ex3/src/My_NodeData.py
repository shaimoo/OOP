from Geolocation import Geolocation
from NodeData import NodeData



class My_NodeData(NodeData, Geolocation):


    def __init__(self):
        self.setlocation(self)
        self.tag = 0
        #key = id
        self.key = 0
        self.info = ""
        self.Tag_ =0
        self.Weight = 0.0
        self.prev = 0

    def __int__(self, o=NodeData):
        self.setlocation(self)
        self.tag = o.getTag
        # key = id
        self.key = o.getkey
        self.info = o.getInfo
        self.Tag_ = o.getTag
        self.Weight = o.getWeight
        self.prev = o.getPrev()

    def getkey(self) -> int:
        return super().getkey()

    def getlocation(self) -> Geolocation:
        return super().getlocation()

    def setlocation(self, Geolocation) -> None:
        super().setlocation(Geolocation)

    def getWeight(self) -> float:
        return super().getWeight()

    def setPrev(self, int) -> None:
        super().setPrev(int)

    def getPrev(self) -> int:
        return super().getPrev()

    def setWeight(self, float) -> None:
        super().setWeight(float)

    def getInfo(self) -> str:
        return super().getInfo()

    def setInfo(self, str) -> None:
        super().setInfo(str)



