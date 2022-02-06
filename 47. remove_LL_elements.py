# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        #Dummy head
        dummy_head = ListNode()
        dummy_head.next = head
        
        current_node = dummy_head
        prev_node = current_node
        
        while current_node:
            
            next_node = current_node.next
            
            if current_node.val == val:
                
                prev_node.next = next_node
                current_node = prev_node
                
            if next_node == None:
                return dummy_head.next
                
            prev_node = current_node
            current_node = current_node.next
        
            
        return dummy_head.next
                
            
        
