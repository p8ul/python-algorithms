"""
Graph Search
- G = (V,E)
- V = set of vertices
- E = set of edges

Applications
- Web crawling
- Social networking
- Network broadcast
- Garbage collection
- Model checking
- Checking mathematical conj
- Solving puzzles &  games

Hamiltonian path
- It is a path in an undirected or directed graph that visits each vertex exactly once
- Hamiltonian cycle is a Hamiltonian path that is a cycle
- Determining whether such paths and cycles exists in graphs is NP-complete!!
- Travelling salesman problem relies on Hamiltonian cycles
- TSP problem: given a list of cities and the distances between each pair of cities, what is the shortest
  possible route that visits each city exactly once and returns to the origin city?
- If there is a Hamiltonian path for a graph: it is the solution for the travelling salesman problem
- NP-complete problem

Eulerian path
- It is a trail in a graph which visits every edge exactly once
- Eulerian cycle is an Eulerian trail which starts and ends on the same vertex
- an undirected graph has an Eurelian cycle if and only if every vertex has even degree
- We can construct graphs that has Eulerian cycles with Heirholzer algorithm ...
  important for the Chinese Postman Problem
- Chinese postman problem: a postman needs to go through every street at least once + closed +
  wants to find a shortest path
- If there is an Eulerian cycle -> that is the solution for the CPP!!

Breadth First search
- We visit every vertex exactly once
- We visit each neighbour vertex then the neighbours of these new vertices
- Running time of the algorithm: O(V+E)
- It has to store a lot of pointers so it is not as efficient as depth first search
- It construct shortest path tree: Dijkstra shortest path algorithm does a BFS if all the edge weight are
  equal to 1
- In AI /machmine learning it can prove to be very important: robots can discover the sorrounding more easily with
  BSF than DFS
- It is also very important in maximum flow: the Edmonds-Karp maximum flow algorithm uses
  BFS for finding augmenting paths
- Cheyen's Algorithm in garbage collection: similar to mark and sweep gc procedure, it helps to maintain the active
  references -> it uses BFS to detect all the references on the heap memory.
"""