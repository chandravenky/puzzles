def find_disappeared_numbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
     
    result1 = [0]*len(nums)
    result2 = []
    
    for i in range(0, len(nums)):
        
        if result1[nums[i]-1]==0:
            result1[nums[i]-1] = nums[i]
        
        else:
            pass
    
    for i in range(0, len(result1)):

      if i +1 != result1[i]:
        result2.append(i+1)



    return result2
