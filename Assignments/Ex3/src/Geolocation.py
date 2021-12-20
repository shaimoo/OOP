class Geolocation:
    """
       This interface represents a geo location <x,y,z>, (aka Point3D data).
    """


    def getX(self) -> float :
        """
        :return:
        """
    def getY(self) -> float :
            """
            :return:
            """

    def getZ(self) -> float :
            """
            :return:
            """

    def setXYZ(self,*args) -> None:
        """
        set the Geolocation
        :param int:
        :return:
        """

    def Distance(self,Geolocation) -> float:
        """
        :param Geolocation:
        :return:the distance from this node to other node
        """