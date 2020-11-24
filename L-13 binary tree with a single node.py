# Construct a binary tree with a single node
# J. RAGHURAMJEE 121910313004

class TreeNode:

	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def printhead(self):
		print(self.data)

treenode = TreeNode(35)
treenode.printhead()