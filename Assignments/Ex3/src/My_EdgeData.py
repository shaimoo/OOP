from EdgeData import EdgeData

class My_EdgeData(EdgeData):

     def __init__(self ,src:int,dest:int,weight:float):

          self.Src=src
          self.Dest=dest
          self.Weight=weight
          self.Info=""
          self.Tag=-1


     def getSrc(self) -> int:
          return self.Src

     def getDest(self) -> int:
          return self.Dest

     def getWeight(self) -> float:
          return self.Weight

     def getInfo(self) -> str:
          return self.Info

     def setInfo(self, x:str) -> None:
          self.Info=x

     def getTag(self) -> int:
          return self.Tag

     def setTag(self, x:int) -> None:
          self.Tag=x

     def __str__(self) -> str:
        return "Our_Proj._EdgeData{" +\
          "Src=" + str(self.getSrc()) +\
          ", Dest=" + str(self.getDest()) +\
          ", Weight=" + str(self.getWeight()) +\
          ", Info='" + str(self.getInfo()) + '\'' +\
          ", Tag=" + str(self.getTag()) +\
          '}'


     def __repr__(self) -> str:
          return "Our_Proj._EdgeData{" + \
          "Src=" + str(self.getSrc()) + \
            ", Dest=" + str(self.getDest()) + \
            ", Weight=" + str(self.getWeight()) + \
            ", Info='" + str(self.getInfo()) + '\'' + \
            ", Tag=" + str(self.getTag()) + \
            '}'


