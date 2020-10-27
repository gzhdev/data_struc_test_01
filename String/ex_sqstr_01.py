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


class SqString(IString):
    def __init__(self, obj=None):
        if obj is None:  # 构造空串
            self.strValue = []  # 字符数组存放串值
            self.curLen = 0
        elif isinstance(obj, str):  # 判断obj是否为字符串，以字符串构造串
            self.curLen = len(obj)
            self.strValue = [None] * self.curLen
            for i in range(self.curLen):
                self.strValue[i] = obj[i]
        elif isinstance(obj, list):  # 以字符列表构造串
            self.curLen = len(obj)
            self.strValue = [None] * self.curLen
            for i in range(self.curLen):
                self.strValue[i] = obj[i]

    def allocate(self, newCapacity):
        tmp = self.strValue
        self.strValue = [None] * newCapacity
        for i in range(self.curLen):
            self.strValue[i] = tmp[i]

    def clear(self):
        self.curLen = 0

    def isEmpty(self):
        return self.curLen == 0

    def length(self):
        return self.curLen

    def charAt(self, i):
        if i < 0 or i >= self.curLen:
            raise IndexError("String index out of range")
        return self.strValue[i]

    def subString(self, begin, end):
        if begin < 0 or begin >= end or end > self.curLen:
            raise IndexError("参数不合法")
        tmp = [None] * (end - begin)
        for i in range(begin, end):
            tmp[i - begin] = self.strValue[i]
        return SqString(tmp)

    def insert(self, i, str):
        if i < 0 or i > self.curLen:
            raise IndexError("插入位置不合法")
        length = len(str)
        newCapacity = self.curLen + length
        self.allocate(newCapacity)
        for j in range(self.curLen - 1, i - 1, -1):
            self.strValue[j + length] = self.strValue[j]
        for j in range(i, i + length):
            # print(j-i,str.charAt(j-i))
            self.strValue[j] = str[j - i]
        self.curLen = newCapacity

    def delete(self, begin, end):
        if begin < 0 or begin >= end or end > self.curLen:
            raise IndexError("参数不合法")
        for i in range(begin, end):
            self.strValue[i] = self.strValue[i + end - begin]
        self.curLen = self.curLen - end + begin

    def concat(self, str):
        self.insert(self.curLen, str)

    def compareTo(self, str):
        n = self.curLen if self.curLen < len(str) else len(str)
        for i in range(n):
            if self.strValue[i] > str[i]:
                return 1
            if self.strValue[i] < str[i]:
                return -1
        if self.curLen > len(str):
            return 1
        elif self.curLen < len(str):
            return -1
        return 0

    def indexOf(self, str, begin):
        if len(str) <= self.curLen and str is not None and self.curLen > 0:
            i = begin
            length = len(str)
            while i <= self.curLen - length:
                for j in range(length):
                    if str[i] != self.strValue[j + i]:
                        i += 1
                        break
                    elif j == length - 1:
                        return i
        return -1

    def display(self):
        for i in range(self.curLen):
            print(self.strValue[i], end=' ')


'''
# (1) 创建串s="abcdefghefghijklmn"和串s1="xyz"
str0 = "abcdefghefghijklmn"
str1 = "xyz"
s = SqString(str0)
s1 = SqString(str1)
# (2) 输出串s。
s.display()
print("\n", end="")
# (3) 输出串s的长度。
print(s.length())
# # (4) 在串s的第9个字符位置插入串s1而产生串s2。
# s2 = SqString(s.strValue)
# s2.insert(9, s1.strValue)
# # (5) 输出串s2。
# s2.display()
# # (6) 删除串s的第2个字符开始的5个字符而产生串s2。
# s2 = SqString(s.strValue)
# s2.delete(2, 7)
# # (7) 输出串s2。
# s2.display()
# (8) 将串s的第2个字符开始的5个字符替换成串s1而产生串s2。
s2 = SqString(s.strValue)
s2.delete(2, 7)
s2.insert(2,s1.strValue)
# (9) 输出串s2。
s2.display()
print("\n", end="")
# (10) 提取串s的第2个字符开始的10个字符而产生串s3。
s3 = s.subString(2,12)
# (11) 输出串s3。
s3.display()
print("\n", end="")
# (12) 将串s1和串s2连接起来而产生串s4。
s4 = SqString(s1.strValue)
s4.concat(s2.strValue)
# (13) 输出串s4。
s4.display()
'''

