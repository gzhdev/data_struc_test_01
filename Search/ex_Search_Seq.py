class RecordNode(object):  # 记录节点类
    def __init__(self, key, data):
        self.key = key  # 关键字
        self.data = data  # 数据元素的值


class SqList:  # 顺序表类

    def __init__(self, maxsize):
        self.curLen = 0  # 当前长度
        self.maxSize = maxsize  # 最大长度
        self.listItem = [None] * (self.maxSize + 1)  # 顺序表储存空间

    def clear(self):
        self.curLen = 0

    def isEmpty(self):
        return self.curLen == 0

    def length(self):
        return self.curLen

    def get(self, i):  # 读取第i个元素
        if i < 0 or i > self.curLen-1:
            raise Exception("第i个元素不存在")
        return self.listItem[i]

    def insert(self, i, x):  # i为插入位置，x为插入的值
        if self.curLen == self.maxSize:
            raise Exception("顺序表满")
        if i < 0 or i > self.curLen:
            raise Exception("插入位置非法")
        for j in range(self.curLen, i-1, -1):
            self.listItem[j] = self.listItem[j-1]
        self.listItem[i] = x
        self.curLen += 1

    def remove(self, i):  # 删除第i个元素
        if i < 0 or i > self.curLen-1:
            raise Exception("删除位置非法")
        for j in range(i, self.curLen-1):
            self.listItem[j] = self.listItem[j+1]
        self.curLen -= 1

    def indexOf(self, x):  # 返回元素x首次出现的序号
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        for i in range(self.curLen):
            print(self.listItem[i].data, end=' ')

    def seqSearch(self, key):  # 顺序查找
        for i in range(self.length()):
            if self.listItem[i].key == key:
                return self.listItem[i].data
        return -1


# (1) 初始化一个静态查找表StaticTable。
StaticTable = SqList(11)
# (2) 判断StaticTable是否为空。
print(StaticTable.isEmpty())
# (3) 将关键字为 (3, 6, 2, 10, 1, 8, 5, 7, 4, 9) 的序列依次存入表StaticTable中。
keys = [3, 6, 2, 10, 1, 8, 5, 7, 4, 9]
for i in keys:
    StaticTable.insert(StaticTable.length(), RecordNode(i, i))
# (4) 遍历StaticTable，并输出所有元素。
StaticTable.display()
print(' ')
# (5) 采用顺序查找算法查找关键字为5的数据元素。
print(StaticTable.seqSearch(5))




