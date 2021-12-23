from Assignments.Ex3.src.My_Geolocation import My_Geolocarion
from Geolocation import Geolocation
from NodeData import NodeData


class My_NodeData(NodeData):

    def __init__(self, key=int , t=tuple):
            self.key = key
            self.location = t
            self.prev = -1
            self.Weight=-1

    def getkey(self) -> int:
        x=int(self.key)
        return x

    def getlocation(self) -> tuple:
        x=tuple(self.location)
        return x

    def setlocation(self,tuple) -> None:
        self.location= tuple

    def getWeight(self) -> float:
        x=float(self.Weight)
        return x

    def setPrev(self, x: int) -> None:
        self.prev= x

    def getPrev(self) -> int:
        return self.prev

    def setWeight(self, x:float) -> None:
        self.Weight = x

    def getInfo(self) -> str:
        return self.info

    def setInfo(self, x:str) -> None:
        self.info=x

    def __str__(self) -> str:
        s = "------ Node #" + str(self.key) + " ------\n" + \
            "   - Info = " + self.info + "   -Wight  " + str(self.getWeight)

        return s

    def __repr__(self) -> str:
        s = "------ Node #" + str(self.key) + " ------\n" + \
            "   - Info = " + self.info + "   -Wight  " + str(self.getWeight)

        return s

    def __eq__(self, o: object) -> bool:
        return self.__eq__(o)
