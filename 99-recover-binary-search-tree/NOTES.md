While doing an in-order traversal of the BST, instead of an ordered list, we will find an almost ordered list where only two places have been swapped. Our goal is to poit to the nodes corresponding to these swapped values.
​
So, we only need to find where the obtained sequences stop increasing, and later when it does stop decreasing.