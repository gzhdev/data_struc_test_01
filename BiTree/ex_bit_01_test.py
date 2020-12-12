from BiTree.ex_bit_01 import BiTree

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
# (2)
ins = "BDCEAFHG"
pos = "DECBHGFA"
testTreeNode2 = BiTree().creatBiTree2(pos, ins, 7, 7, 8)
testTree2 = BiTree(testTreeNode2)
testTree2.postOrder()
print()
testTree2.inOrder()
print()
testTree2.perOrder()
print()
testTree2.order()
# (3) ABC##DE#G##F###
testTreeNode3 = BiTree().creatBiTree3()
testTree3 = BiTree(testTreeNode3)
testTree3.perOrder()
print()
testTree3.inOrder()
print()
testTree3.postOrder()