import math

from Geolocation import Geolocation


class My_Geolocarion(Geolocation):


    def __init__(self, o=Geolocation,x=int ,y=int ,z=int ): ##maybe if end else needed
       if o==None:
             self.setXYZ(x,y,z)
       else:
             self.setXYZ(o.getX, o.getY, o.getZ)

    def Distance(self, Geolocation) -> float:
        dis = math.sqrt(self.getX()**2-Geolocation.getX()**2 + self.getY()**2-Geolocation.getY()**2
                      + self.getZ()**2-Geolocation.getZ()**2)
        return dis


    def getX(self) -> float:
        return super().getX()

    def getY(self) -> float:
        return super().getY()

    def getZ(self) -> float:
        return super().getZ()

    def setXYZ(self, *args) -> None:
        super().setXYZ(*args)

    def __str__(self) -> str:
        s = " Coord (x,y,z) = ( " + str(self.getX()) + " , " + str(self.getY()) + " , " + str(self.getZ())

        return s

    def __repr__(self) -> str:
        s = " Coord (x,y,z) = ( " + str(self.getX()) + " , " + str(self.getY()) + " , " + str(self.getZ())

        return s
