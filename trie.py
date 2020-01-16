class TriNode:
	def __init__(self):
		self.children = {}
		self.endOfWord = False


class Trie:
	def __init__(self):
		self.root = TriNode()

	#Time Complexity
	def add(self, word):
		currentNode = self.root
		for char in word:
			if char not in currentNode.children:
				print("inserting ", char)
				node = TriNode()
				currentNode.children[char] = node
			currentNode = currentNode.children[char]

		currentNode.endOfWord = True


	def find(self, w):
		currentNode = self.root
		for char in w:
			if char not in currentNode.children:
				return False
			currentNode = currentNode.children[char]

		return currentNode.endOfWord


	


	path = ""
	def printDFS(self, root):
		if not root:
			return

		if root.endOfWord:
			print(path)

		for char, node in root.children.items():
			path = path + char
			self.printDFS(node)




trie = Trie()
trie.add("abc")
#trie.printDFS(trie.root)



