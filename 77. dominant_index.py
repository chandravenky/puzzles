

#Problem 747

def dominant_index(nums):

  largest_num = -99999999999999
        
  for i in range(0, len(nums)):
    
    if nums[i] > largest_num:
      largest_num = nums[i]
      largest_index = i
        
  for i in range(0, len(nums)):
      
    if i==largest_index:
      pass
      
    else:
      if nums[i]*2 > largest_num:
        return -1
          
  return largest_index
