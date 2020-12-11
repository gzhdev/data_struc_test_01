from abc import ABCMeta, abstractmethod, abstractproperty


class IGraph(metaclass=ABCMeta):
    @abstractmethod
    def creatGraph(self):
        pass

    @abstractmethod
    def getVNum(self):
        # 返回图中的顶点数
        pass

    @abstractmethod
    def getENum(self):
        # 返回图中的边数
        pass

    @abstractmethod
    def getVex(self, i):
        # 返回位置为i的顶点值
        pass

    @abstractmethod
    def locateVex(self, x):
        # 返回值为x的顶点位置
        pass

    @abstractmethod
    def firstAdj(self, i):
        # 返回节点的第一个邻接点
        pass

    @abstractmethod
    def nextAdj(self, i, j):
        # 返回相对于j的下一个邻接点
        pass
