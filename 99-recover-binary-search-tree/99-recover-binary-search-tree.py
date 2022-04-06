# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        #in-order traversal
        stack = []
        current = root
        
        #Pointers to nodes where the in-order sequence changes monotonically behaivor
        MaxNode = None
        MinNode = None
        
        #Keeps track of previous node processed
        PrevNode = None
        
        #Vars to keep trak of max and min values
        Max = float('-inf')
        Min = float('inf')
        
        while (stack or current!= None):
            #Go to leftmost node
            while current != None:
                stack.append(current)
                current = current.left
                
            #Process it, i.e. verify there is no change in monotonicity
            current = stack.pop()
            
            if not bool(MaxNode):
                if current.val > Max:
                    Max = current.val
                else:
                    MaxNode = PrevNode
                    
            if bool(MaxNode) and  current.val > MaxNode.val:
                MinNode = PrevNode
                break
                    
            PrevNode = current
            current = current.right
        
        #If MinNode is still empty, then it is the last node of the in-ordered sequence
        if   MinNode == None:
            MinNode = PrevNode
            
        #Swap values between MaxNode and MinNode
        temp = MaxNode.val
        MaxNode.val = MinNode.val
        MinNode.val = temp
                    
                
            
            
            