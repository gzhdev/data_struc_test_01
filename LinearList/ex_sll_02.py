from LinearList.ex_sll_01 import LinkList

# 创建链表SLLa及SLLb
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
SLLa = LinkList()
SLLb = LinkList()
SLLa.creat(a, True)
SLLb.creat(b, True)
# 合并算法
SLLc = LinkList()

pa = SLLa.head.next
pb = SLLb.head.next
pc = SLLc.head
while pa is not None and pb is not None:
    if pa.data >= pb.data:
        pc.next = pb
        pb = pb.next
    else:
        pc.next = pa
        pa = pa.next
    pc = pc.next
if pa is not None:
    pc.next = pa
elif pb is not None:
    pc.next = pb


'''
c = []
while SLLa.length() != 0 and SLLb.length() != 0:
    if SLLa.get(0) <= SLLb.get(0):
        c.append(SLLa.get(0))
        SLLa.remove(0)
    else:
        c.append(SLLb.get(0))
        SLLb.remove(0)
SLLc.creat(c, True)

while  SLLa.isEmpty() is not True:
    SLLc.creat_tail([SLLa.get(0)])
    SLLa.remove(0)
while SLLb.isEmpty() is not True:
    SLLc.creat_tail([SLLb.get(0)])
    SLLb.remove(0)
'''
SLLc.display()


