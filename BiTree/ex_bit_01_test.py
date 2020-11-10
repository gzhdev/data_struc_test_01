from BiTree.ex_bit_01 import BiTree

ps = "ABDGCEF"
ins = "DGBAECF"
testTreeNode = BiTree().creatBiTree(ps, ins, 0, 0, 7)
testTree = BiTree(testTreeNode)
print(testTree.perOrder())
# print(testTree.inOrder())
# print(testTree.postOrder())
