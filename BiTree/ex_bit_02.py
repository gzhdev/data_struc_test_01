class HuffmanNode(object):
    def __init__(self, data, weight):
        self.data = data
        self.weight = weight
        self.parent = None
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    def __init__(self, data):
        # data是编码字符与出现次数的集合，例如 w=[('a',1),('b',2)]
        nodes = [HuffmanNode(c, w) for c, w in data]
        self.index = {}  # 编码字符索引
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.weight)
            s = HuffmanNode(None, nodes[0].weight + nodes[1].weight)
            s.lchild = nodes[0]
            s.rchild = nodes[1]
            nodes[0].parent = nodes[1].parent = s
            nodes = nodes[2:]
            nodes.append(s)
        self.root = nodes[0]
        self.calIndex(self.root, '')  # 递归计算每个字符的哈夫曼编码并保存

    def calIndex(self, root, str):
        if root.data is not None:
            # 保存字符的编码
            self.index[root.data] = str
        else:
            self.calIndex(root.lchild, str+'0')
            self.calIndex(root.rchild, str+'1')

    def queryHuffmanCode(self, c):
        if c not in self.index:
            raise Exception("未编码的字符")
        return self.index[c]