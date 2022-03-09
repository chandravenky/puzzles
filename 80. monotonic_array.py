#Problem 896

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = 0
        
        for i in range(0, len(nums)-1):
            
            if nums[i] == nums[i+1]:
                pass
            
            elif nums[i] <= nums[i+1]:
                if flag==0:
                    flag = 1
                
                if flag != 1:
                    return False
                
            elif nums[i] >= nums[i+1]:
                if flag==0:
                    flag = -1
                
                if flag != -1:
                    return False
                
        return True
                
        
