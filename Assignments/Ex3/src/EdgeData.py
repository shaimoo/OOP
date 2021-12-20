class EdgeData:

    """
    This interface represents the set of operations applicable on a
    directional edge(src,dest) in a (directional) weighted graph.
    """
    def getSrc(self) -> int:
        """
        return current src
        """
    def getDest(self) -> int:
        """
        return dest of current edge
        """
    def getWeight(self) -> float:
        """
        return the weight on this Edge
        """
    def getInfo(self) -> str:
        """
        retun the Info assosiated with this edge
        """
    def setInfo(self,str) -> None:
        """
        setting the Info with str
        """
    def getTag(self) -> int:
        """
        returning tag with algo
        """
    def setTag(self,int) -> None:
        """
        setting the tag with algo
        """
