#Solution
def search(nums, target):

  start_pointer = 0
  end_pointer = len(nums)-1

  while start_pointer <= end_pointer:

    current_pointer = (start_pointer + end_pointer)//2

    if nums[current_pointer] == target:
      return current_pointer

    #if left hand side is strictly increasing
    elif nums[current_pointer] - nums[start_pointer]>=0:

      #if target is in left hand side
      if nums[start_pointer] <= target and target <= nums[current_pointer]:
        end_pointer = current_pointer-1
      
      #if target is in right hand side
      else:
        start_pointer = current_pointer + 1
    
    #if left handside is not strictly increasing, then right side is
    else: 

      #if target is in right hand side
      if target <= nums[end_pointer] and target >= nums[current_pointer]:
        
        start_pointer = current_pointer + 1

      #if target is in left hand side
      else:
        
        end_pointer = current_pointer -1
        
  return -1
