1. Take the smalles elements of each heap and push them into a heap.
2. While the heap is not empty:
*    pop smallest element and add it to the list to be returned
*    push to the heap the following element in the list where the poped element          belongs
​
​
Time complexity: O(n* log(k)), where n is the total amount of elements in all the of the lists together and k is the numer of lists