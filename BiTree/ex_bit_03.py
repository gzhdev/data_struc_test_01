from BiTree.ex_bit_01 import BiTree


def nodeCount(t):
    if t is None:
        return 0
    else:
        return nodeCount(t.lchild) + nodeCount(t.rchild) + 1


def leafCount(t):
    if t is None:
        return 0
    if t.lchild is None and t.rchild is None:
        return 1
    else:
        return leafCount(t.lchild) + leafCount(t.rchild)


def getDepth(t):
    if t is None:
        return 0
    else:
        ldepth = getDepth(t.lchild)
        rdepth = getDepth(t.rchild)
        m = ldepth if ldepth > rdepth else rdepth
        return m + 1


# (1)
ps = "ABDGCEF"
ins = "DGBAECF"
testTreeNode = BiTree().creatBiTree(ps, ins, 0, 0, 7)
testTree = BiTree(testTreeNode)
testTree.perOrder()
print()
testTree.inOrder()
print()
testTree.postOrder()
print()
print(nodeCount(testTree.root))
print(leafCount(testTree.root))
print(getDepth(testTree.root))
