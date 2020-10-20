# 节点类描述
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


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
            print(p.data, end=' ')
            p = p.next


'''
# (1)
ll = LinkList()
# (2)
print(ll.isEmpty())
# (3)
value = [33, 24, 231, 3, 11]
ll.creat(value, True)
# (4)
print(ll.length())
# (5)
ll.insert(3, 11)
# (6)
ll.creat_head([25])
# (7)
ll.remove(4)
# (8)
print(ll.get(3))
# (9)
ll.display()
'''
