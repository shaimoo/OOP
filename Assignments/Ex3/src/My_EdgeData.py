from EdgeData import EdgeData

class My_EdgeData(EdgeData):

     def __init__(self , o = EdgeData):
          self.Src=o.getSrc
          self.Dest=o.getDest
          self.Weight=o.getWeight
          self.Info=o.getInfo
          self.Tag=o.getTag


     def getSrc(self) -> int:
          return super().getSrc()

     def getDest(self) -> int:
          return super().getDest()

     def getWeight(self) -> float:
          return super().getWeight()

     def getInfo(self) -> str:
          return super().getInfo()

     def setInfo(self, str) -> None:
          super().setInfo(str)

     def getTag(self) -> int:
          return super().getTag()

     def setTag(self, int) -> None:
          super().setTag(int)

     def __str__(self) -> str:
        return "Our_Proj._EdgeData{" +\
          "Src=" + str(self.getSrc) +\
          ", Dest=" + str(self.getDest) +\
          ", Weight=" + str(self.getWeight) +\
          ", Info='" + str(self.getInfo()) + '\'' +\
          ", Tag=" + str(self.getTag) +\
          '}'


     def __repr__(self) -> str:
          return "Our_Proj._EdgeData{" + \
          "Src=" + str(self.getSrc) + \
            ", Dest=" + str(self.getDest) + \
            ", Weight=" + str(self.getWeight) + \
            ", Info='" + str(self.getInfo()) + '\'' + \
            ", Tag=" + str(self.getTag) + \
            '}'


