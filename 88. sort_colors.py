#Problem 75

def sort_colors(nums):
    
  store = {0: 0, 1: 0, 2: 0}
  
  for i in range(0, len(nums)):
      
    store[nums[i]] = store[nums[i]] + 1
      
  for i in range(0, len(nums)):
      
    if store[0] >0:
      nums[i] = 0
      store[0] = store[0] - 1
    
    elif store[1] > 0:
      nums[i] = 1
      store[1] = store[1] - 1
        
    else:
      nums[i] = 2
      store[2] = store[2] - 1
        
  return nums

def sort_colors_test():

  input_nums1 = [2,0,2,1,1,0]
  input_nums2 = [2,0,1]

  expected_output1 = [0,0,1,1,2,2]
  expected_output2 = [0,1,2]

  return ( expected_output1 == sort_colors(input_nums1), expected_output2 == sort_colors(input_nums2) )

print(sort_colors_test())

#Submission
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        store = {0: 0, 1: 0, 2: 0}
        
        for i in range(0, len(nums)):
            
            store[nums[i]] = store[nums[i]] + 1
            
        for i in range(0, len(nums)):
            
            if store[0] >0:
                nums[i] = 0
                store[0] = store[0] - 1
            
            elif store[1] > 0:
                nums[i] = 1
                store[1] = store[1] - 1
                
            else:
                nums[i] = 2
                store[2] = store[2] - 1
                
        return nums
