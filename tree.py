class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val



def bstInsert(root, node) :
	if root == None:
		return Node(node.val)

	if node.val < root.val:
		root.left = bstInsert(root.left, node)
	else:
		root.right = bstInsert(root.right, node)

	return root


def bstInsertNode(root, node) :
	if root == None:
		return Node(node.val)

	if node.val < root.val:
		newNode = bstInsert(root.left, node)
		root.left = newNode
	else: 
		newNode = bstInsert(root.right, node)
		root.right = newNode

	return newNode


def minValueNode(root):
	current = root
	while(current.left != None):
		current = current.left
	return current

def bstDelete(root, node):
	#when tree is empty
	if root == None:
		return root

	# If node to be deleted is smaller than the root, go left
	if node < root.val:
		root.left = bstDelete(root.left, node)

	#If node to be deleted is greater than the root, go right
	elif(node > root.val):
		root.right = bstDelete(root.right, node)

	# Node to be deleted found
	else:
		#Right child or no child
		if root.left == None:
			temp = root.right
			root = None
			return temp

		#Left child or no child
		elif(root.right == None):
			temp = root.left
			root = None
			return temp

		# 2 children, 
		else:
			# either find predecessor from left subtree (max elem)
			# or successor from the right subtree (smallest elem)
			minValNode =  minValueNode(root.right)

			# assign the value of the successor to the node
			root.val = minValNode.val

			# delete the successor
			root.right = bstDelete(root.right, minValNode.val)

		return root



def inorder(root):
	if root == None:
		return 
	inorder(root.left)
	print(root.val)
	inorder(root.right)


r = Node(50) 
bstInsert(r,Node(30)) 
bstInsert(r,Node(20)) 
bstInsert(r,Node(40)) 
bstInsert(r,Node(70)) 
bstInsert(r,Node(60)) 
bstInsert(r,Node(80)) 

inorder(r)

bstDelete(r, 70)

print("----------------------------")

inorder(r)

