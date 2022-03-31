# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def flip(self, node):

        if not node:
            return None

        hold_node = node.left
        node.left = node.right
        node.right = hold_node

        self.flip(node.left)
        self.flip(node.right)
            
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        self.flip(root)
        
        return root
