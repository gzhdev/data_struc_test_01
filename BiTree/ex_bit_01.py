from Stack.ex_sls_01 import LinkStack
from Queue.ex_lsq_01 import LinkQueue


class BiTreeNode(object):
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree(object):
    def __init__(self, root=None):
        self.root = root

    def perOrder(self):  # 先序遍历
        p = self.root
        s = LinkStack()
        s.push(p)
        while not s.isEmpty():
            p = s.pop()
            print(p.data, end=' ')
            while p is not None:
                if p.lchild is not None:
                    print(p.lchild.data, end=' ')
                if p.rchild is not None:
                    s.push(p.rchild)
                p = p.lchild

    def inOrder(self):  # 中序遍历
        p = self.root
        s = LinkStack()
        while p is not None or not s.isEmpty():
            if p is not None:
                s.push(p)
                p = p.lchild
            else:
                p = s.pop()
                print(p.data, end=' ')
                p = p.rchild

    def postOrder(self):  # 后序遍历
        p = self.root
        s = LinkStack()
        while True:
            while p is not None:
                s.push(p)
                p = p.lchild
            t = None
            flag = True
            while not s.isEmpty() and flag:
                p = s.peek().data
                if p.rchild == t:
                    print(p.data, end=' ')
                    p = s.pop()
                    t = p
                else:
                    p = p.rchild
                    flag = False
            if s.isEmpty():
                break

    def order(self):  # 层次遍历
        q = LinkQueue()
        q.offer(self.root)  # 根节点入队
        while not q.isEmpty():
            p = q.poll()
            print(p.data, end=' ')
            if p.lchild is not None:
                q.offer(p.lchild)
            if p.rchild is not None:
                q.offer(p.rchild)

    def creatBiTree(self, preoString, inoString, preo, ino, n):
        # preoString 存放先序序列，inoString 存放中序序列，preo指向当前先序序列的根节点，ino指向当前中序序列的第一个元素，n为二叉树的节点个数
        if n > 0:
            i = 0
            c = preoString[preo]  # c为先序序列 preoString 的根节点
            while i < n:  # 在中序序列 inoString 中找等于 c 的位置 i
                if inoString[ino + i] == c:
                    break
                i += 1
            root = BiTreeNode(c)
            root.lchild = BiTree().creatBiTree(preoString, inoString, preo+1, ino, i)  # 构造左子树
            root.rchild = BiTree().creatBiTree(preoString, inoString, preo + i + 1, ino + i + 1, n - i - 1)  # 构建右子树
            return root


