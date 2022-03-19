# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        value_array = []
        #Use built in TimSort in python to sort elements - can use HeapSort to do O(1)
        
        current_node = head
        while current_node!= None:
            
            value_array.append(current_node.val)
            current_node = current_node.next
        
        value_array = sorted(value_array)
        new_head = ListNode()
        current_node = new_head
        
        for i in range(0, len(value_array)):
            
            current_node.next = ListNode(value_array[i])
            current_node = current_node.next
            
        return new_head.next
