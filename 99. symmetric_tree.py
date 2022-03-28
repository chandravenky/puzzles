# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root==None:
            return True
        
        return self.check_if_symm(root.left, root.right)
        
    def check_if_symm(self, node1, node2):
        
        if node1==None or node2==None:
            return node1==node2
        
        if node1.val != node2.val:
            return False

        return self.check_if_symm(node1.left, node2.right) and self.check_if_symm(node1.right, node2.left)
        
