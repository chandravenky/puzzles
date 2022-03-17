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
