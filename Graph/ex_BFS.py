from Queue.ex_lsq_01 import LinkQueue


class vNode(object):  # 顶点节点vNode
    def __init__(self, data=None, firstNode=None):
        self.data = data
        self.firstArc = firstNode  # 指向与该节点相关联的第一条边


class ArcNode(object):
    def __init__(self, adjVex, value, nextArc=None):
        self.adjVex = adjVex  # 该边所指向的顶点的位置
        self.value = value  # 权值
        self.nextArc = nextArc  # 指向与该顶点相关联的下一条边


class ALGraph:
    GRAPHKIND_UDG = 'UDG'  # 无向图
    GRAPHKIND_DG = 'DG'  # 有向图
    GRAPHKIND_UDN = 'UDN'  # 无向网
    GRAPHKIND_DN = 'DN'  # 有向网

    def __init__(self, kind=None, vNum=0, eNum=0, v=None, e=None):
        self.kind = kind  # 图的种类
        self.vNum = vNum  # 图的顶点数
        self.eNum = eNum  # 图的边数
        self.v = v  # 顶点列表
        self.e = e  # 边信息

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
        return self.v[i].data

    def locateVex(self, x):
        # 返回值为x的顶点位置
        for i in range(self.vNum):
            if self.v[i].data == x:
                return i
        return -1

    def firstAdj(self, i):
        if i < 0 or i > self.vNum:
            raise Exception("第%s个顶点不存在" % i)
        if self.v[i].firstArc is not None:
            return self.v[i].firstArc.adjVex
        return -1

    def nextAdj(self, i, j):
        # 返回相对于j的下一个邻接点
        v = self.v[i].firstArc
        if v is None:
            return -1
        while v.adjVex != j and v is not None:
            v = v.nextArc
        if v is None or v.nextArc is None:
            return -1
        else:
            return v.nextArc.adjVex

    def addArc(self, i, j, value=1):
        arc = ArcNode(j, value)  # 创建一个边节点，邻接点序号为j，边的权值是value
        arc.nextArc = self.v[i].firstArc  # 将新的边节点插入顶点v[i]的边表头部
        self.v[i].firstArc = arc

    def createUDG(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.vNum):  # 创建顶点表
            self.v[i] = vNode(v[i])
        for i in range(self.eNum):  # 创建边表
            a, b = self.e[i]  # 获取一组边的信息
            u, v = self.locateVex(a), self.locateVex(b)  # 确定a和b在顶点列表中的位置，w为权值
            self.addArc(u, v)
            self.addArc(v, u)

    def createDG(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.vNum):  # 创建顶点表
            self.v[i] = vNode(v[i])
        for i in range(self.eNum):  # 创建边表
            a, b = self.e[i]  # 获取一组边的信息
            u, v = self.locateVex(a), self.locateVex(b)  # 确定a和b在顶点列表中的位置，w为权值
            self.addArc(u, v)

    def createUDN(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.vNum):  # 创建顶点表
            self.v[i] = vNode(v[i])
        for i in range(self.eNum):  # 创建边表
            a, b, w = self.e[i]  # 获取一组边的信息
            u, v = self.locateVex(a), self.locateVex(b)  # 确定a和b在顶点列表中的位置，w为权值
            self.addArc(u, v, w)
            self.addArc(v, u, w)

    def createDN(self):
        v = self.v
        self.v = [None] * self.vNum
        for i in range(self.vNum):  # 创建顶点表
            self.v[i] = vNode(v[i])
        for i in range(self.eNum):  # 创建边表
            a, b, w = self.e[i]  # 获取一组边的信息
            u, v = self.locateVex(a), self.locateVex(b)  # 确定a和b在顶点列表中的位置，w为权值
            self.addArc(u, v, w)


def BFS(g, i, visited):
    print(g.getVex(i), end=' ')  # 访问顶点i
    visited[i] = True
    q = LinkQueue()  # 创建空队列
    q.offer(i)  # 顶点i入队
    while not q.isEmpty():  # 若队列非空
        u = q.poll()  # 队头元素出队并设置为u
        v = g.firstAdj(u)  # 查找u的第一个邻接点v
        while v != -1:  # 若v存在
            if not visited[v]:  # v为u的尚未访问的邻接顶点
                print(g.getVex(v), end=' ')
                visited[v] = True
                q.offer(v)  # 顶点v入队
            v = g.nextAdj(u, v)


def BFSTraverse(g):
    for i in range(g.getVNum()):  # 建立访问标志数组
        visited = [False] * g.getVNum()
        BFS(g, i, visited)
        print()


v0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
e0 = [
    ('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'E'), ('C', 'F'), ('D', 'G'), ('E', 'G'),
    ('G', 'H'), ('H', 'I')]
g0 = ALGraph(ALGraph.GRAPHKIND_UDG, len(v0), len(e0), v0, e0)
g0.creatGraph()
visited0 = [False] * len(v0)
BFS(g0, 0, visited0)
