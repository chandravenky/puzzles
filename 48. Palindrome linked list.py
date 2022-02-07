# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        current_node = head
        num_string = ""
        
        while current_node:
            
            num_string = num_string + str(current_node.val)
            current_node = current_node.next
            
        reversed_num_string = num_string[::-1]
        
        if num_string == reversed_num_string:
            return True
        
        return False
