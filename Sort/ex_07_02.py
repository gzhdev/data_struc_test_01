# 节点类描述
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class RecordNode(object):  # 记录节点类
    def __init__(self, key, data):
        self.key = key  # 关键字
        self.data = data  # 数据元素的值


# 单链表类描述
class LinkList:
    def __init__(self):
        self.head = Node()  # 构造函数初始化头节点

    def creat(self, l, order):
        if order:
            self.creat_tail(l)
        else:
            self.creat_head(l)

    def creat_tail(self, l):  # 尾插法
        for item in l:
            self.insert(self.length(), item)

    def creat_head(self, l):  # 头插法
        for item in l:
            self.insert(0, item)

    def clear(self):
        self.head.data = None
        self.head.next = None

    def isEmpty(self):
        return self.head.next is None

    def length(self):
        p = self.head.next
        length = 0
        while p is not None:
            p = p.next
            length += 1
        return length

    def get(self, i):
        p = self.head.next
        j = 0
        while j < i and p is not None:
            p = p.next
            j += 1
        if j > i or p is None:
            raise Exception("第" + i + "个元素不存在")
        return p.data

    def insert(self, i, x):
        p = self.head
        j = -1
        while p is not None and j < i - 1:
            p = p.next
            j += 1
        if j > i - 1 or p is None:
            raise Exception("插入位置不合法")
        s = Node(x, p.next)
        p.next = s

    def remove(self, i):
        p = self.head
        j = -1
        while p is not None and j < i - 1:
            p = p.next
            j += 1
        if j > i - 1 or p.next is None:
            raise Exception("删除位置不合法")
        p.next = p.next.next

    def indexOf(self, x):
        p = self.head.next
        j = 0
        while p is not None and not (p.data == x):
            p = p.next
            j += 1
        if p is not None:
            return j
        else:
            return -1

    def display(self):
        p = self.head.next
        while p is not None:
            print(p.data.data, end=' ')
            p = p.next

    def insertSort_lklist(self):
        # 进行len-1次扫描
        for i in range(1, self.length()):
            p = self.get(i)
            self.remove(i)
            # 从list[i-1]起向前顺序查找插入位置
            j = i - 1
            while j >= 0:
                if self.get(j).key > p.key:  # 逆序时
                    # self.insert(j, p)
                    # self.remove(i)
                    j -= 1
                else:
                    break
            self.insert(j+1, p)


# (1) 初始化一个单链表lklist。
lklist = LinkList()
# (2) 通过insert()方法，将待排序的关键字序列data = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36] 依次存入单链表lklist中。
data = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36]
for i in data:
    lklist.insert(lklist.length(), RecordNode(i, i))
# (3) 遍历lklist，并输出所有元素。
lklist.display()
print('')
# (4) 调用insertSort_lklist()方法对序列lklist进行直接插入排序。
lklist.insertSort_lklist()
# (5) 遍历lklist，并输出所有元素。
lklist.display()
