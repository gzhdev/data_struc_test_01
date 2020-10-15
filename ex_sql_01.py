class SqList():
    def __init__(self, maxsize):
        self.curLen = 0 #当前长度
        self.maxSize = maxsize #最大长度
        self.listItem = [None] * (self.maxSize + 1) #顺序表储存空间

    def clear(self):
        self.curLen = 0

    def isEmpty(self):
        return self.curLen == 0

    def length(self):
        return self.curLen

    def get(self, i): #读取第i个元素
        if i < 0 or i > self.curLen-1:
            raise Exception("第i个元素不存在")
        return self.listItem[i]

    def insert(self, i, x): #i为插入位置，x为插入的值
        if self.curLen == self.maxSize:
            raise Exception("顺序表满")
        if i < 0 or i > self.curLen:
            raise Exception("插入位置非法")
        for j in range(self.curLen, i-1, -1):
            self.listItem[j] = self.listItem[j-1]
        self.listItem[i] = x
        self.curLen += 1

    def remove(self, i): #删除第i个元素
        if i < 0 or i > self.curLen-1:
            raise Exception("删除位置非法")
        for j in range(i, self.curLen-1):
            self.listItem[j] = self.listItem[j+1]
        self.curLen -= 1

    def indexOf(self, x): #返回元素x首次出现的序号
        for i in range(self.curLen):
            if self.listItem[i] == x:
                return i
        return -1

    def display(self):
        for i in range(self.curLen):
            print(self.listItem[i], end=' ')

'''
SQL = SqList(20)
print(SQL.isEmpty())
data = [2, 5, 16, 55, 8]
for i in range(len(data)):
    SQL.insert(i, data[i])
print(SQL.length())
print(SQL.indexOf(5)+1)
SQL.insert(SQL.indexOf(5)+1, 11)
SQL.remove(0)
SQL.display()
SQL.clear()
'''