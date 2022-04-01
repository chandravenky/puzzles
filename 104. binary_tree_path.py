# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        output = []
        
        def path(root, curr):
            if not root:
                return
            
            #if leaf comes
            if root.left==None and root.right==None:
                output.append(curr + str(root.val))
            
            path(root.left, curr + str(root.val) + "->")
            path(root.right, curr + str(root.val) + "->")
            
        
        path(root, '')
        
        return output
        
