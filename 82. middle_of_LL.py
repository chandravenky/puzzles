#Problem 876

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        current_node = head
        
        while current_node != None:
            
            length = length + 1
            
            current_node = current_node.next
            
        mid_index = length//2
        
        current_index = 0
        current_node = head
        while current_index != mid_index:
            
            current_node = current_node.next
            current_index = current_index + 1
        

        return current_node
        
