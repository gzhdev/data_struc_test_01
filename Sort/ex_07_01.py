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

    # 插入排序
    def insertSort(self):  # 直接插入排序
        # 进行len-1次扫描
        for i in range(1, self.curLen):
            p = self.listItem[i]
            # 从list[i-1]起向前顺序查找插入位置
            j = i - 1
            while j >= 0:
                if self.listItem[j].key > p.key:  # 逆序时
                    self.listItem[j + 1] = self.listItem[j]  # 将关键字大于list[i].key的记录后移
                    j -= 1
                else:
                    break
            self.listItem[j + 1] = p  # 在j+1处插入list[i]

    # 希尔排序
    def shellSort(self, d):
        for dk in d:
            for i in range(dk, self.curLen):
                # 对相隔dk位置的元素组直接插入排序
                p = self.listItem[i]
                # 比list[i]大的元素后移dk个位置
                j = i - dk
                while j >= 0:
                    if self.listItem[j].key > p.key:
                        self.listItem[j + dk] = self.listItem[j]
                        j -= dk
                    else:
                        break
                self.listItem[j + dk] = p

    # 冒泡排序
    def bubbleSort(self):
        flag = True  # 用于标记某趟排序是否发生交换
        i = 1
        while i < self.curLen and flag:
            flag = False  # flag置为0，若本趟没发生交换，则不会执行下趟排序
            for j in range(self.curLen - i):
                # 比较本趟最大关键字的记录
                if self.listItem[j + 1].key < self.listItem[j].key:  # 逆序则交换
                    p = self.listItem[j]
                    self.listItem[j] = self.listItem[j + 1]
                    self.listItem[j + 1] = p
                    flag = True
            i += 1

    # 快速排序
    def qSort(self, low, high):
        if low < high:  # 基本结束条件
            p = self.Partition(low, high)  # 一次划分，p是支点位置
            self.qSort(low, p - 1)  # 递归对前半子列进行快速排序
            self.qSort(p + 1, high)  # 递归对后半子列进行快速排序

    def Partition(self, low, high):
        p = self.listItem[low]  # 选定支点
        while low < high:  # 从两端交替向中间扫描，直到low==high为止
            while low < high and self.listItem[high].key >= p.key:
                # 从右向左扫描，找一个key小于p.key的listItem[high]
                high -= 1
            if low < high:
                # 找到这样的list[high]，放入low处
                self.listItem[low] = self.listItem[high]
                low += 1
            while low < high and self.listItem[low].key <= p.key:
                # 从左向右扫描，找一个key大于p.key的list[low]
                low += 1
            if low < high:
                # 找到这样的list[low],放入high处
                self.listItem[high] = self.listItem[low]
                high -= 1
        self.listItem[low] = p
        return low

    # 直接选择排序
    def selectSort(self):
        for i in range(self.curLen - 1):  # 进行n-1趟排序
            # 在list[i...len-1]中寻找关键字最小的记录
            tmp = i
            for j in range(i + 1, self.curLen):
                if self.listItem[j].key < self.listItem[tmp].key:
                    tmp = j  # tmp存放此趟排序中关键字最小的位置
            # 交换位置
            if tmp != i:
                p = self.listItem[i]
                self.listItem[i] = self.listItem[tmp]
                self.listItem[tmp] = p

    # 堆排序
    def sift(self, low, high):  # 堆调整
        i = low
        j = 2 * i + 1  # list[j]是list[i]的左孩子
        p = self.listItem[i]
        while j <= high:
            if j < high and self.listItem[j].key < self.listItem[j + 1].key:
                # 比较左右孩子的关键字大小
                j += 1  # 指示大孩子
            if p.key < self.listItem[j].key:  # 双亲小于大孩子
                self.listItem[i] = self.listItem[j]  # 将list[j]调整到双亲结点位置
                i = j  # 修改i和j的位置，以便继续向下筛选
                j = 2 * i + 1
            else:
                break  # 双亲大不再调整
        self.listItem[i] = p

    def heapSort(self):
        for i in range(self.curLen // 2 - 1, -1, -1):  # 建立循环初始堆
            self.sift(i, self.curLen - 1)
        for i in range(self.curLen - 1, 0, -1):  # 进行n-1次循环，完成堆排序
            p = self.listItem[0]
            self.listItem[0] = self.listItem[i]
            self.listItem[i] = p  # 堆顶元素归位
            self.sift(0, i - 1)  # 筛选list[0]结点，得到i个结点的堆

    # 归并排序
    def merge(self, order, a, i, k, j):  # 两个相邻有序序列归并
        t = i
        m = i
        n = k + 1
        while m <= k and n <= j:
            # 将具有较小关键字的值的元素放入order[]
            if a[m].key <= a[n].key:
                order[t] = a[m]
                t += 1
                m += 1
            else:
                order[t] = a[n]
                t += 1
                n += 1
        while m <= k:
            order[t] = a[m]
            t += 1
            m += 1
        while n <= j:
            order[t] = a[n]
            t += 1
            n += 1

    def mergepass(self, order, a, s, n):  # 一趟归并排序
        p = 0
        while p + 2 * s - 1 <= n - 1:  # 两两归并长度均为s的有序表
            self.merge(order, a, p, p + s - 1, p + 2 * s - 1)
            p = p + 2 * s
        if p + s - 1 < n - 1:  # 归并长度不等的有序表
            self.merge(order, a, p, p + s - 1, n - 1)
        else:  # 将一个有序表的元素放入order[]中
            for i in range(p, n):
                order[i] = a[i]

    def mergeSort(self):  # 二路归并排序
        s = 1  # 已排序的子序列的长度，初始值是1
        order = [None] * self.curLen
        while s < self.curLen:  # 归并过程
            self.mergepass(order, self.listItem, s, self.curLen)
            s = s * 2
            self.mergepass(self.listItem, order, s, self.curLen)
            s = s * 2


# (1) 初始化一个顺序表sqlist。
sql = SqList(10)
# (2) 通过insert()方法，将待排序的关键字序列data = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36] 依次存入顺序表sqlist中。
data = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36]
for i in data:
    sql.insert(sql.length(), RecordNode(i, i))
# (3) 遍历sqlist，并输出所有元素。
sql.display()
print('')
# (4) 调用insertSort()方法对序列sqlist进行直接插入排序。
sql.insertSort()
# (5) 遍历sqlist，并输出所有元素。
sql.display()
# (6) 调用shellSort()方法对序列sqlist进行希尔排序，增量为5，3，1。
d = [5, 3, 1]
sql.shellSort(d)
# (7) 遍历sqlist，并输出所有元素。
sql.display()
print('')
# (8) 调用bubbleSort()方法对序列sqlist进行冒泡排序。
sql.bubbleSort()
# (9) 遍历sqlist，并输出所有元素。
sql.display()
print('')
# (10) 调用qSort()方法对序列sqlist进行快速排序。
sql.qSort(0, 9)
# (11) 遍历sqlist，并输出所有元素。
sql.display()
print('')
# (12) 调用selectSort()方法对序列sqlist进行直接选择排序。
sql.selectSort()
# (13) 遍历sqlist，并输出所有元素。
sql.display()
print('')
# (14) 调用heapSort()方法对序列sqlist进行堆排序。
sql.heapSort()
# (15) 遍历sqlist，并输出所有元素。
sql.display()
print('')
# (14) 调用mergeSort()方法对序列sqlist进行归并排序。
sql.mergeSort()
# (15) 遍历sqlist，并输出所有元素。
sql.display()
print('')