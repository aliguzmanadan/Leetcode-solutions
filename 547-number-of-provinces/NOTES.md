The idea is to create a DisjointSet structure with a function returning the amount of islands in it.
One idea for this is to go throguh all roots and check how many different roots are there.
Anoter is to have a counter of different islands (initialized to n) and reduce it every time we effectively connect two cities.