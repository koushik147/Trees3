class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maximum = root.val # craeting maximum
        self.recur(root) # calling recur function
        return self.maximum # returning maximum
    
    def recur(self,root):
        #base condition
        if root == None:
            return 0
        
        leftSum = max(self.recur(root.left),0) # calculating the leftsum by calling recur function
        rightSum = max(self.recur(root.right),0) # calculating the rightsum by calling recur function
        
        rootmax = root.val + leftSum + rightSum # calculating rootmax with root value
        
        if self.maximum < rootmax:
            self.maximum = rootmax # assigning the maximum value
            
        return root.val + max(leftSum,rightSum) # returning root value + maximum between leftsum and rightsum