class RecordNode(object):  # 记录节点类
    def __init__(self, key, data):
        self.key = key  # 关键字
        self.data = data  # 数据元素的值


class SqList:
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
        if i < 0 or i > self.curLen - 1:
            raise Exception("第i个元素不存在")
        return self.listItem[i]

    def insert(self, i, x):  # i为插入位置，x为插入的值
        if self.curLen == self.maxSize:
            raise Exception("顺序表满")
        if i < 0 or i > self.curLen:
            raise Exception("插入位置非法")
        for j in range(self.curLen, i - 1, -1):
            self.listItem[j] = self.listItem[j - 1]
        self.listItem[i] = x
        self.curLen += 1

    def remove(self, i):  # 删除第i个元素
        if i < 0 or i > self.curLen - 1:
            raise Exception("删除位置非法")
        for j in range(i, self.curLen - 1):
            self.listItem[j] = self.listItem[j + 1]
        self.curLen -= 1

    def indexOf(self, x):  # 返回元素x首次出现的序号
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        for i in range(self.curLen):
            print(self.listItem[i].data, end=' ')

    def binarySearch(self, key):
        if self.length() > 0:
            low = 0
            high = self.curLen - 1
            while low < high:
                mid = (low + high) // 2
                if self.listItem[mid].key == key:
                    return mid  # 查到待查元素
                elif self.listItem[mid].key < key:  # 查找范围为后半部分
                    low = mid + 1
                else:  # 查找范围为前半部分
                    high = mid - 1
            return -1  # 表中不存在待查元素


# (1) 初始化一个静态查找表StaticTable。
StaticTable = SqList(10)
# (2) 判断StaticTable是否为空。
StaticTable.isEmpty()
# (3) 将关键字为 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 的序列依次存入表StaticTable中。
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in keys:
    StaticTable.insert(StaticTable.length(), RecordNode(i, i))
# (4) 遍历StaticTable，并输出所有元素。
StaticTable.display()
print(' ')
# (5) 采用二分查找算法查找关键字为9的数据元素。
print(StaticTable.binarySearch(9))

