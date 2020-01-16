import math
import os
import random
import re
import sys

sys.setrecursionlimit(100007)


# Complete the 'hasCycle' function below.
#
# The function accepts INTEGER N, INTEGER M and 2D_INTEGER_ARRAY edges as parameter.
# The function is expected to return a BOOLEAN.
#
from collections import defaultdict

def construct_graph(adj, edges):
    for cell in edges:
        adj[cell[0]].add(cell[1])
        

def dfs(adj,stack, visited,edges, N):
	

	construct_graph(adj, edges)
    
	for vertex in range(0, N):
		dfs_util(adj, visited, vertex)

    
	return 


def dfs_util(adj, visited, vertex):
    # print("vertex being visited")
    # print(vertex)
    # print("--------")



    if vertex in visited:
        return
    
    visited.add(vertex)
    
    for neighbor in adj[vertex]:
    	dfs_util(adj, visited, neighbor)
    
    
   

    print("vertex visited completely")
    print(vertex)
    print("--------")
    return 
    

def hasCycle(N, M, edges):
    # Write your code here
    adj = defaultdict(set)
    
    visited, stack = set(), set()
    
    construct_graph(adj, edges)
    return dfs(adj,stack, visited, N)



if __name__ == "__main__":
    N = int(input().strip())
    M = int(input().strip())

    edges = []

    adj = defaultdict(set)

    visited, stack = set(), set()

    for _ in range(M):
        edges.append(list(map(int, input().rstrip().split())))

    fptr = sys.stdout

    # result = hasCycle(N, M, edges)

    dfs(adj,stack, visited,edges, N)

    #fptr.write(str(int(result)) + '\n')



    fptr.close()