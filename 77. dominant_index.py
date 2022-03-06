

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

def dominant_index_test():

  input_nums1 = [3,6,1,0]
  input_nums2 = [1,2,3,4]
  input_nums3 = [1]

  expected_output1 = 1
  expected_output2 = -1
  expected_output3 = 0

  return ( expected_output1 == dominant_index(input_nums1), expected_output2 == dominant_index(input_nums2), expected_output3 == dominant_index(input_nums3)  )

print(dominant_index_test())
