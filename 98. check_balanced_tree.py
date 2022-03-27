#Problem 110
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_balanced(root)[0]
    
    def check_balanced(self, root):
        if root == None:
            return True, 0
        
        else:
            left_node = self.check_balanced(root.left)
            right_node = self.check_balanced(root.right)
            
            if left_node[0] and right_node[0] and abs(left_node[1] - right_node[1])<=1:
                return True, max(left_node[1], right_node[1]) +1
            
            else:
                return False, max(left_node[1], right_node[1]) +1
            
        
