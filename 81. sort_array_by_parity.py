#Problem 905

#Try inplace
class Solution(object):
  def sortArrayByParity(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    holding_pointer = 0
    
    for i in range(0, len(nums)):
      
      if nums[i]%2==0:
        holding_num = nums[holding_pointer]
        nums[holding_pointer] = nums[i]
        nums[i] = holding_num
        
        holding_pointer = holding_pointer + 1
            
    return nums
            
        
    
