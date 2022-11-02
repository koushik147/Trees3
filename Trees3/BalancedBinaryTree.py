#Time_Complexity: O(n) 
#Space_Complexity : O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque() # declaring queue
        q.append(root) # appending root in queue
        
        while q:
            size = len(q) # storing length of q
            level = [] # creating level array
            for i in range(size): 
                currElement = q.popleft() # popping from q and save it in currElement
                if currElement != None:
                    level.append(currElement.val) # appending the value in level
                    q.append(currElement.left) # appending in q the left of root
                    q.append(currElement.right) # appending in q the right of root
                else:
                    level.append(currElement) # appending the currElement in level 
                
            if not(self.isPalindrome(level)): # if level is not palindrome then return false
                return False 
        return True
    
    def isPalindrome(self,li): 
        left = 0 # craeting left with 0
        right = len(li) - 1 # creating right with length of li
        
        while left <= right: # run until left is less than right
            if li[left] != li[right]: # if left is not equal to right then return false
                return False 
            left += 1
            right -= 1
            
        return True
