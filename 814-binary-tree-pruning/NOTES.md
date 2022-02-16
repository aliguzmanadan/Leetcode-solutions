This can be omplemented recursively following a bottom-up approach.
​
If we denote the act of prunning all zero subtrees of a tree with root at "root" by Prune(root), then
​
Prune(root){
Prune(root.left);
Prune(root.right);
if root.val == 0 and Prune(root.left) == None and Prune(root.right) ==. None:
return None
}