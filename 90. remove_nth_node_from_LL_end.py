# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        slow_pointer = 0
        fast_pointer = 0
        
        slow_pos = head
        fast_pos = head
        
        while True:
            
            count = 0
            while count <=n and fast_pos != None:
                fast_pos = fast_pos.next
                
                if fast_pos == None:
                    break
                
                fast_pointer = fast_pointer + 1
                count= count+1
            
            if fast_pos == None and slow_pointer == fast_pointer - n:
                
                current_node = slow_pos
                nextNext_node = slow_pos.next.next
                current_node.next = nextNext_node
                
                return head
            
            if fast_pointer-n<0:
                return head.next
            
            slow_pos = slow_pos.next
            slow_pointer = slow_pointer + 1
        
