### Bellman-Ford Algorithm
- computes shortest paths from a single source vertex to all the other vertices in a weighted diagraph.
- slower than Dijkstra's algorithm but more versatile
- running time is O(V*E)
- Does V-1 iteration + 1 to detect cycles: if cost decreases in the V-th iteraction
  than there is a negative cycle, because all the paths are traversen up to the 
  V-1 iteration!
  

#### Application
- Routing Information Protocol
- This a distributed algorithm
1) Each node calculates the distance betweeen itself and all other nodes and
  stores this information as a table
 2) Each node sends its table to all adjacent nodes
 3) When a node receives distance tables from its neighbors, it calculates
 the shortest routes to all other nodes and updates its own table to 
 reflect any changes