from Assignments.Ex3.src.My_Geolocation import My_Geolocarion
from Geolocation import Geolocation
from NodeData import NodeData



class My_NodeData(NodeData, Geolocation):



    def __init__(self, o=NodeData):
        self.location = o.getlocation
        self.tag = o.getTag
        # key = id
        self.key = o.getkey
        self.info = o.getInfo
        self.Tag_ = o.getTag
        self.Weight = o.getWeight
        self.prev = o.getPrev


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

    def __str__(self) -> str:
        s = "------ Node #" + str (self.key) + " ------\n" +\
            "   - Info = " + self.info + "   -Wight  " +str (self.getWeight)

        return s

    def __repr__(self) -> str:
        s = "------ Node #" + str(self.key) + " ------\n" + \
            "   - Info = " + self.info + "   -Wight  " + str(self.getWeight)

        return s

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)





