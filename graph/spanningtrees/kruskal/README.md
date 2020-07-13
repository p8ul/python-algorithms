### Kruskal Algorithm
- [Kruskal algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) Is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that connects any two in the forest.
- Is a greedy algorithm in graph theory
- We sort edges according to their edge weights
- Edge weights are invariant under the transformation of these weights (addition, multiplication)
- I can be done in O(N logN) with mergesort or quicksort
- Union find data structure: "disjoint set""
  We start adding edges to the MST and we want to ake sure there will be no cycles in the spanning tree. It can be done in O(logV)
  with the help of union find data structure
  
 
[REF](https://www.youtube.com/watch?v=JZBQLXgSGfs) 