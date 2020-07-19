## Graph coloring
- coloring the vertices of a graph such that no two adjacent vertices share the same color
- Vertex coloring
- chromatic number: the smallest number of colors needed to color a graph G

### Application
#### Bipartite graphs
- Determining if a graph can be colored with 2 colors is equivalent to determining whether or not the graph is bipartite,
and thus computable in linear time using breadth-first search
- Bipartite graph: a graph whose vertices can be divided into two disjoint sets U and V ( U and V are independent sets) such that every edge connects a vertex in U to one in V

#### Making schedule
- We want to make an exam schedule for a university. We have different subjects and different students enrolled on every subject. Many subjects would have common students.
- How do we schedule the exam so that no two exams with a common student are scheduled at the same time? How many minimum time slots are needed to schedule all exams?
- This problem can be represented as a graph where every vertex is a subject and an edge between two vertices means there is a common studen. So this is a graph coloring problem where minimum number of time slots is equal to chromatic number of graph

#### Radio frequency assignment
- When frequencies are assigned to towers, frequencies assigned to all towers at the same location must be different because of he interference!!
- How to assign frequencies with this constraints? What is the minimum number of frequencies needed?
- This problem is also an instance of graph coloring problem where every tower represents a vertex and an edge between two towers represents that they are in range of each other.

#### Register allocation
- In compiler optimization, register allocation is the process of assigning a large number of target program variables onto a small number of CPU registers.

#### Map coloring
- We want to construct a map of countries or states where adjacent countries or states cannot be assigned the same color
- Four colors are sufficient to color any map