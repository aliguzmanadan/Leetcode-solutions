The idea is: There is a path from A to B if and onl if there is a path from A to a neighbor of B.

We can implement this recursively and iteratively. Doing it recursively is very straighforward. 

T do it iteratively, we need to do a DFS strating from the source vertex and then adding each non-visited neighbor to a stack. While the stack is not empty, we then pop the top element, and proceess it accordingly (see code).
