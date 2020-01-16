from collections import defaultdict, deque
from pprint import pprint

class Graph:
	def __init__(self, connections, vertices, directed = False):
		self.adj = defaultdict(set)
		self.directed = directed
		self.vertices = vertices
		self.construct_graph(connections)


	def construct_graph(self, connections):
		for node1, node2 in connections:
			self.add_edge(node1, node2)


	def add_edge(self, node1, node2):
		self.adj[node1].add(node2)

		if not self.directed:
			self.adj[node2].add(node1)


# -------------------- Topo Sort using out degrees ------------------- # 

	def get_out_degrees(self, out_degree, zero_degree):
		for vertex in self.vertices:
			for neighbor in self.adj[vertex]:
				if vertex not in out_degree:
					out_degree[vertex] = 1
				else:
					out_degree[vertex] += 1

		for vertex in self.vertices:
			if vertex not in out_degree:
				zero_degree.append(vertex)

		pprint(out_degree)
		pprint(zero_degree)

	def adjust_out_degrees(self, out_degree, zero_degree, node):
		for vertex in self.vertices:
			for neighbor in self.adj[vertex]:
				if neighbor == node:
					prev_degree = out_degree[vertex]
					out_degree[vertex] -=1
					if prev_degree == 1:
						zero_degree.append(vertex)

	def topo_sort_out_degree(self):
		topo_sort, zero_degree = [], []
		out_degree = {}
	

		self.get_out_degrees(out_degree, zero_degree)

		while zero_degree:
			node = zero_degree.pop()
			topo_sort.append(node)
			self.adjust_out_degrees(out_degree, zero_degree, node)

		print("------------Topo sort is:---------")
		length = len(topo_sort)
		for i in range(length):
			print(topo_sort.pop())

# -------------------- Topo Sort using in degrees ------------------- # 

	def get_in_degrees(self, in_degrees, zero_degree):
		for vertex in self.vertices:
			for neighbor in self.adj[vertex]:
				if neighbor in in_degrees:
					in_degrees[neighbor] +=1
				else:
					in_degrees[neighbor] =1

		for vertex in self.vertices:
			if vertex not in in_degrees:
				zero_degree.append(vertex)


	def update_in_degrees(self, in_degrees, zero_degree, vertex):
		for neighbor in self.adj[vertex]:
			prev_degree = in_degrees[neighbor]
			in_degrees[neighbor] -= 1

			if prev_degree == 1:
				zero_degree.append(neighbor)


	def topo_sort_in_degree(self):
		zero_degree = []
		result = deque()
		in_degrees = {}


		self.get_in_degrees(in_degrees, zero_degree)

		while zero_degree:
			node = zero_degree.pop()
			result.append(node)
			self.update_in_degrees(in_degrees, zero_degree, node)


		print("-------------topo sort in degrees---------")
		length = len(result)
		for i in range(0, length):
			print(result.popleft())





vertices = [1, 2, 3, 4, 5, 6, 7]
connections = [(1, 2), (1, 4), (2, 3), (4, 3), (3, 5), (5, 6), (5, 7), (6, 7)]

g = Graph(connections,vertices, True)

g.topo_sort_out_degree()

g.topo_sort_in_degree()













