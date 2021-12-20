from Geolocation import Geolocation


class NodeData:

    def getkey(self) -> int:
        """
        return the key of the node
        """

    def getlocation(self) -> Geolocation:
        """
        return the location of the node
        """

    def setlocation(self, Geolocation) -> None:
        """
        change the location of the node
        return:None
        """

    def getWeight(self) -> float:
        """
        return the Weight of the node

        """

    def setWeight(self, float) -> None:
        """
        changing the weight of the node
        """

    def getInfo(self) -> str:
        """
        :return the Info of the node
        """

    def setInfo(self, str) -> None:
        """
        changing the Info of the node
        :return None
        """

    def getTag(self) -> int:
        """
         :return the Tag of node
        """

    def setTag(self, int) -> None:
        """
                set the Tag of the node
                :param int:
                :return: None
                """
    def setPrev(self, int ) -> None:
        """
        this represent father
        """
    def getPrev(self) -> int:
        """
        return prev
        """
