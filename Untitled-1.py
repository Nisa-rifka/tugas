class TreeNode:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(11)
node7 = TreeNode(7)
node15 = TreeNode(15)
node13 = TreeNode(13)
node19 = TreeNode(19)
node12 = TreeNode(12)
node14 = TreeNode(14)

root.left = node7
root.right = node15

node15.left = node13
node15.right = node19

node13.left = node12
node13.right = node14

print("munculah nilai nya:", root.right.left.left.data)