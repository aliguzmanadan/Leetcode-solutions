e sThe idea is to use two heaps:
​
* heap_smaller : containing all the values smaller than the median (to keep the maximum at the root we multiply by -1 before pushing into the heap)
* heap_bigger: ontaining all the values bigger than the median
While adding new values to the structure, we keep the two heaps with the same size (or with a difference of 1 in size) so that we can easily track the median back.