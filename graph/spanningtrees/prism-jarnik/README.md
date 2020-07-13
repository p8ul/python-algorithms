### Prism-Jarnik Algorithm
- A greedy [algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) that finds a minimum spanning tree for a weighted unidrected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.
- We build the spanning tree separately, adding the smallest edge to the spanning tree if there is no cycle
- Two implementation: Lazy & Eager
- Lazy: add the new neighbour edges to the heap without deleting its content
- Eager: we keep updating the heap if the distance from a vertex to the MST has changed
- Average running time: O (E logE) but we need additional memory for O(E)
- Worst case: O(E logV)