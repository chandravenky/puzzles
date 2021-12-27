#Solution 1
def search_and_insert(nums, target):

  for i in range(0, len(nums)):

    if target == nums[i]:
      return i

    elif target <nums[i]:
      return i
    
  return i+1
