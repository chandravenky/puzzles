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

#Tests
def find_disappeared_numbers_test():

  input_array1 = [4,3,2,7,8,2,3,1]
  input_array2 = [1,1]

  expected_output1 = [5,6]
  expected_output2 = [2]


  return ( expected_output1 == find_disappeared_numbers(input_array1), expected_output2 == find_disappeared_numbers(input_array2) )


print(find_disappeared_numbers_test())
