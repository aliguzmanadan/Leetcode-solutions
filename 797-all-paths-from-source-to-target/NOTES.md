Main idea:
Given the start A and the destination B. The paths from A to B are given by

            Paths(A,B) = [A + Paths(C,B) for all C directed neighbors of A]

We don't need to keep track of the visited nodes since it is a directed acyclic graph.
This can be implemented recursively using DFS.
