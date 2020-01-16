
from collections import defaultdict
from pprint import pprint
from collections import deque

# Graph implementation using adjacency list, 
# Used python dictionary of sets to build adjacency list
class Graph(object):
	def __init__(self, connections, vertices, directed = False):
		self.graph = defaultdict(set) # adjacency list
		self.directed = directed
		self.vertices = vertices
		self.add_connections(connections)


	def add_connections(self, connections):
		for node1, node2 in connections:
			self.add(node1, node2)


	def add(self, node1, node2):
		# add connecion between node1 and node2
		self.graph[node1].add(node2)
		if not self.directed:
			self.graph[node2].add(node1)


	def bfs_queue(self, adj, src):
		queue = deque([src])
		visited = set(src)

		while queue:
			node = queue.popleft()
			print(node)
			for neighbor in adj[node]:
				if neighbor not in visited:
					visited.add(neighbor)
					queue.append(neighbor)



	def bfs(self, src, adj):
		level, parent = {}, {}
		frontier = [src]

		parent[src] = None
		level[src] = 0
		i = 1

		while frontier:
			next = []
			for u in frontier:
				for v in adj[u]:
					if v not in level:
						level[v] = i
						parent[v] = u
						next.append(v)

			i = i + 1
			frontier = next
			pprint(frontier)

		print("--------------------")
		print("Level")
		pprint(level)
		print("--------------------")
		print("Parent")
		pprint(parent)


	def dfs_visit(self, src, adj, parent):
		print("Visiting ", src, "'s neighbors recursively")
		for v in adj[src]:
			if v not in parent:
				parent[v] = src
				self.dfs_visit(v, adj, parent)

		


	def dfs(self, vertices, adj):
		parent = {}
		for src in vertices:
			if src not in parent:
				parent[src] = None
				self.dfs_visit(src, adj, parent)
		print("--------------------")
		print("Parent")
		pprint(parent)



	def topo_sort_dfs(self, adj, vertices):
		visited = set()
		stack = []

		for vertex in vertices:
			if vertex in visited:
				continue
			self.topo_sort_dfs_util(adj, stack, visited, vertex)
		return stack



	def topo_sort_dfs_util(self, adj, stack, visited, vertex):
		visited.add(vertex)
		for neighbor in adj[vertex]:
			if neighbor not in visited:
				self.topo_sort_dfs_util(adj, stack, visited, neighbor)

		stack.append(vertex)
	
	

	def get_degrees(self, adj,vertices, zero_degree, in_degree):

		# Calculate the in degrees of the verices
		for vertex in vertices:
			for neighbor in adj[vertex]:
				if neighbor in in_degree:
					in_degree[neighbor] += 1
				else:
					in_degree[neighbor] = 1


		# get vertices with zero degree
		for vertex in vertices:
			if vertex not in in_degree:
				zero_degree.append(vertex)


	def update_degrees(self, adj, vertices, zero_degree, in_degree, vertex):
		# Update the degrees of the neighbors of the given vertex
		for neighbor in adj[vertex]:
			prev_degree = in_degree[neighbor]
			in_degree[neighbor] -= 1

			if prev_degree == 1:
				zero_degree.append(neighbor)



	def topo_sort_bfs(self, adj, vertices):
		zero_degree = []
		in_degree = defaultdict() # what if no default dict ?

		# get in-degrees of each vertex and get vertices with zero degree
		self.get_degrees(adj, vertices, zero_degree, in_degree)

		while zero_degree:
			vertex = zero_degree.pop()

			print(vertex)

			self.update_degrees(adj, vertices, zero_degree, in_degree, vertex)


	













vertices = [1, 2, 3, 4, 5, 6]
connections = [(3, 4), (3, 1), (1, 4), (4, 2), (1, 2), (4, 5), (1, 6), (6, 5)]
vertices = ['s','a', 'x', 'z', 'd', 'c', 'f', 'v' ]
connections = [('s','a'), ('s','x'), ('a','z'), ('x','d'), ('x','c'), ('d','f'), ('c','f'), ('c','v'), ('c', 'd')]

g = Graph(connections,vertices, True)
pprint(g.graph)

print("------------------- BFS ------------------------")
#g.bfs('a', g.graph)
g.bfs_queue(g.graph, 's')

#print("-------------------- DFS -----------------------")
#g.dfs(g.vertices,g.graph)


# print("--------------- Topo DFS ---------------")
#stack = g.topo_sort_dfs(g.graph, vertices)
#pprint(stack)

print("----------------- Topo Sort Kahn's----------------")
g.topo_sort_bfs(g.graph, vertices)








