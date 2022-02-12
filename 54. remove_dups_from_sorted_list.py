# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        store = dict()
        
        dummy_node = ListNode(0)
        dummy= dummy_node
        traverse_node = head
        
        while traverse_node:
            
            if traverse_node.val in store.keys():
                traverse_node = traverse_node.next
                
            else:
                store[traverse_node.val] = 1
                dummy.next = ListNode(traverse_node.val)
                dummy = dummy.next
                traverse_node = traverse_node.next
                
        # dummy.next = None
        
        return dummy_node.next
    
            
