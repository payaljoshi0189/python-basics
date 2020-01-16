from collections import defaultdict

class Graph:
	def __init__(self, edges, vertices, directed = False):
		self.adj = defaultdict(set)
		self.vertices = vertices
		self.directed = directed
		self.add_edges(edges)


	def add_edges(self, edges):
		for node1, node2 in edges:
			self.add_edge(node1, node2)

	def add_edge(self, node1, node2):
		self.adj[node1].add(node2)

		if not self.directed:
			self.adj[node2].add(node1)


	def is_eulerian_cycle_undirected(self):
		degree_count = {}
		for vertex in self.vertices:
			count = 0
			for neighbor in self.adj[vertex]:
				count +=1
			degree_count[vertex] = count

		for count in degree_count.values():
			if count % 2 != 0:
				return False
		return True


	def is_eulerian_cycle_directed(self):
		
		in_degree, out_degree = defaultdict(lambda:0), defaultdict(lambda:0)

		# Compute in degrees and out degrees for each vertex
		for vertex in self.vertices:
			for neighbor in self.adj[vertex]:
				in_degree[neighbor] += 1
				out_degree[vertex] +=1

		for vertex in self.vertices:
			if vertex in in_degree and vertex in out_degree:
				if in_degree[vertex] != out_degree[vertex]:
					return False

		return True



		



connections1 = [(0,1), (0, 3), (1, 2), (2, 3), (0, 5), (5, 3), (4, 0), (4, 1), (7, 1), (7, 2), (6, 3), (6, 2)]
vertices1 = [0, 1, 2, 3, 4, 5, 6, 7]

connections2 = [(0, 1),(1, 3), (3, 4), (1, 2), (2, 0)]
vertices2 = [0, 1, 2, 3, 4]

g1 = Graph(connections1,vertices1)

g2 = Graph(connections2,vertices2, True)

is_eulerian = g1.is_eulerian_cycle_undirected()
print(is_eulerian)


is_eulerian_directed = g2.is_eulerian_cycle_directed()
print(is_eulerian_directed)



