import sys
from Graph.Graph import IGraph


class MGraph(IGraph):
    GRAPHKIND_UDG = 'UDG'  # 无向图
    GRAPHKIND_DG = 'DG'  # 有向图
    GRAPHKIND_UDN = 'UDN'  # 无向网
    GRAPHKIND_DN = 'DN'  # 有向网

    def __init__(self, kind=None, vNum=0, eNum=0, v=None, e=None):
        self.kind = kind  # 图的种类
        self.vNum = vNum  # 图的顶点数
        self.eNum = eNum  # 图的边数
        self.v = v  # 顶点列表
        self.e = e  # 邻接矩阵

    def creatGraph(self):
        if self.kind == self.GRAPHKIND_UDG:
            self.createUDG()
        elif self.kind == self.GRAPHKIND_DG:
            self.createDG()
        elif self.kind == self.GRAPHKIND_UDN:
            self.createUDN()
        elif self.kind == self.GRAPHKIND_DN:
            self.createDN()

    def getVNum(self):
        return self.vNum

    def getENum(self):
        return self.eNum

    def getVex(self, i):
        # 返回位置为i的顶点值
        return self.v[i]

    def locateVex(self, x):
        # 返回值为x的顶点位置
        for i in range(self.vNum):
            if self.v[i] == x:
                return i
        return -1

    def firstAdj(self, i):
        # 返回节点的第一个邻接点
        if i < 0 or i > self.vNum:
            raise Exception("第%s个顶点不存在" % i)
        for j in range(self.vNum):
            if self.e[i][j] != 0 and self.e[i][j] < sys.maxsize:
                return j
        return -1

    def nextAdj(self, i, j):
        # 返回相对于j的下一个邻接点
        if j == self.vNum - 1:
            return -1
        for k in range(j + 1, self.vNum):
            if self.e[i][k] != 0 and self.e[i][k] < sys.maxsize:
                return k
        return -1

    def createUDN(self):
        e = [[sys.maxsize] * self.vNum for i in range(self.eNum - 1)]  # 初始化邻接矩阵，边的权值都设为最大值sys.maxsze
        for i in range(self.eNum):  # 构造邻接矩阵
            a, b, w = self.e[i]
            m, n = self.locateVex(a), self.locateVex(b)
            e[m][n] = e[n][m] = w
        self.e = e

    def createDN(self):
        e = [[sys.maxsize] * self.vNum for i in range(self.eNum - 1)]  # 初始化邻接矩阵，边的权值都设为最大值sys.maxsze
        for i in range(self.eNum):  # 构造邻接矩阵
            a, b, w = self.e[i]
            m, n = self.locateVex(a), self.locateVex(b)
            e[m][n] = w
        self.e = e

    def createUDG(self):
        e = [[0] * self.vNum for i in range(self.eNum - 1)]
        for i in range(self.eNum):
            a, b = self.e[i]
            m, n = self.locateVex(a), self.locateVex(b)
            e[m][n] = e[n][m] = 1
        self.e = e

    def createDG(self):
        e = [[0] * self.vNum for i in range(self.eNum - 1)]
        for i in range(self.eNum):
            a, b = self.e[i]
            m, n = self.locateVex(a), self.locateVex(b)
            e[m][n] = 1
        self.e = e


def DFS(g, i, visited):
    print(g.getVex(i), end=' ')  # 访问顶点i
    visited[i] = True
    v = g.firstAdj(i)  # 查找i的第一个邻接点v
    while v != -1:  # 若v存在
        if not visited[v]:
            DFS(g, v, visited)  # 若v未被访问则递归调用DFS
        v = g.nextAdj(i, v)  # 查找i相对于v的下一个邻接点


def DFSTraverse(g):  # 以每个顶点作为起始顶点开始遍历
    for i in range(g.getVNum()):
        # 建立访问标志数组
        visited = [False] * g.getVNum()
        DFS(g, i, visited)
        print()


v0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
e0 = [
    ('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'E'), ('C', 'F'), ('D', 'G'), ('E', 'G'),
    ('G', 'H'), ('H', 'I')]
g0 = MGraph(MGraph.GRAPHKIND_UDG, len(v0), len(e0), v0, e0)
g0.creatGraph()
visited0 = [False] * g0.getVNum()
DFS(g0, 0, visited0)
