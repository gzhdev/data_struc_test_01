from abc import ABCMeta, abstractmethod, abstractproperty


class IString(metaclass=ABCMeta):
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def allocate(self, newCapacity):
        '''串内容不变，但将串的容量扩充为newCapacity'''
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def charAt(self, i):
        '''读取并返回串中的第i个数据元素'''
        pass

    @abstractmethod
    def subString(self, begin, end):
        '''返回位序号从begin到end-1的子串'''
        pass

    @abstractmethod
    def insert(self, i, str):
        pass

    @abstractmethod
    def delete(self, begin, end):
        pass

    @abstractmethod
    def concat(self, str):
        '''将str连接到字符串后面'''
        pass

    @abstractmethod
    def compareTo(self, str):
        '''比较str和当前字符串的大小'''
        pass

    @abstractmethod
    def indexOf(self, str, begin):
        '''从位序号为begin的字符开始搜索与str相等的子串'''
        pass


# 节点类描述
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkString(IString):
    def __init__(self):
        self.head = Node()  # 构造函数初始化头节点

    def creat(self, obj, order):
        if isinstance(obj, str):
            if order:
                self.creat_tail(obj)
            else:
                self.creat_head(obj)
        elif isinstance(obj, list):
            if order:
                self.creat_tail(obj)
            else:
                self.creat_head(obj)

    def creat_tail(self, str):  # 尾插法
        self.insert(self.length(), str)

    def creat_head(self, str):  # 头插法
        self.insert(0, str)

    def clear(self):
        self.head.data = None
        self.head.next = None

    def allocate(self, newCapacity):  # 无必要，pass
        pass

    def isEmpty(self):
        return self.head.next is None

    def length(self):
        p = self.head.next
        length = 0
        while p is not None:
            p = p.next
            length += 1
        return length

    def charAt(self, i):
        p = self.head.next
        j = 0
        while j < i and p is not None:
            p = p.next
            j += 1
        if j > i or p is None:
            raise Exception("第" + i + "个元素不存在")
        return p.data

    def subString(self, begin, end):
        if begin < 0 or begin >= end or end > self.length():
            raise IndexError("参数不合法")
        tmp = []
        for i in range(begin, end):
            tmp.append(self.charAt(i))
        substr = LinkString()
        substr.creat(tmp, True)
        return substr

    def insert(self, i, obj):
        for m in range(len(obj)):
            p = self.head
            j = -1
            while p is not None and j < i - 1:
                p = p.next
                j += 1
            if j > i - 1 or p is None:
                raise Exception("插入位置不合法")
            s = Node(obj[m], p.next)
            p.next = s
            i += 1

    def delete(self, begin, end):
        c = 1
        while c <= (end - begin):
            c += 1
            p = self.head
            j = -1
            while p is not None and j < begin - 1:
                p = p.next
                j += 1
            if j > begin - 1 or p.next is None:
                raise Exception("删除位置不合法")
            p.next = p.next.next

    def concat(self, lls):
        tmp = []
        for i in range(lls.length()):
            tmp.append(lls.charAt(i))
        self.creat_tail(tmp)

    def compareTo(self, str):
        n = self.length() if self.length() < len(str) else len(str)
        for i in range(n):
            if self.charAt(i) > str[i]:
                return 1
            if self.charAt(i) < str[i]:
                return -1
        if self.length() > len(str):
            return 1
        elif self.length() < len(str):
            return -1
        return 0

    def indexOf(self, str, begin):  # BF
        if len(str) <= self.length() and str is not None and self.length() > 0:
            i = begin
            length = len(str)
            while i <= self.length() - length:
                for j in range(length):
                    if str[i] != self.charAt(j + i):
                        i += 1
                        break
                    elif j == length - 1:
                        return i
        return -1

    def display(self):
        p = self.head.next
        while p is not None:
            print(p.data, end=' ')
            p = p.next


# (1) 创建串s="abcdefghefghijklmn"和串s1="xyz"
print("(1)")
s = LinkString()
s1 = LinkString()
s.creat("abcdefghefghijklmn", True)
s1.creat("xyz", True)
# (2) 输出串s。
s.display()
print("\n", end='')
# (3) 输出串s的长度。
print("(3)")
print(s.length())
# (4) 在串s的第9个字符位置插入串s1而产生串s2。
print("(4)")
s2 = LinkString()
s2.concat(s)
list0 = []
for i in range(s1.length()):
    list0.append(s1.charAt(i))
s2.insert(9, list0)
# (5) 输出串s2。
s2.display()
print("\n", end='')
# (6) 删除串s的第2个字符开始的5个字符而产生串s2。
print("(6)")
s2 = LinkString()
s2.concat(s)
s2.delete(2, 7)
# (7) 输出串s2。
s2.display()
print("\n", end='')
# (8) 将串s的第2个字符开始的5个字符替换成串s1而产生串s2。
print("(8)")
s2 = LinkString()
s2.concat(s)
s2.delete(2, 7)
list1 = []
for i in range(s1.length()):
    list1.append(s1.charAt(i))
s2.insert(2, list1)
# (9) 输出串s2。
s2.display()
print("\n", end='')
# (10) 提取串s的第2个字符开始的10个字符而产生串s3。
print("(10)")
s3 = s.subString(2, 12)
# (11) 输出串s3。
s3.display()
print("\n", end='')
# (12) 将串s1和串s2连接起来而产生串s4。
print("(12)")
s4 = LinkString()
s4.concat(s1)
s4.concat(s2)
# (13) 输出串s4。
s4.display()
print("\n", end='')
