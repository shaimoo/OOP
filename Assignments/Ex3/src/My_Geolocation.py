import math

from Geolocation import Geolocation


class My_Geolocarion(Geolocation):

    def __init__(self):
        self.setXYZ(0.0, 0.0, 0.0)

    def __int__(self, Geolocation):
        self.setXYZ(Geolocation.getX(), Geolocation.getY(), Geolocation.getZ())

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
