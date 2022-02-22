#Problem 485


def max_consecutive_ones(nums):

  max_count =0
  count = 0
  prev = 0
  
  if nums == [1]:
    return 1
    
  for i in range(0, len(nums)):
    print(i)
    if nums[i]==1:
      
      if prev==1:
        count=count+1

      else:
        count = 1
      prev = 1

    else:
      prev= 0 

    if count> max_count:
      max_count = count

  return max_count

#Tests
def max_consecutive_ones_test():

  input_nums1 = [1,1,0,1,1,1]
  input_nums2 = [1,0,1,1,0,1]
  input_nums3 = [1]
  input_nums4 = [0,0]
  input_nums4 = [1,1,0,1]

  expected_output1 = 3
  expected_output2 = 2
  expected_output3 = 1
  expected_output4 = 2

  return ( expected_output1 == max_consecutive_ones(input_nums1), expected_output2 == max_consecutive_ones(input_nums2), expected_output3 == max_consecutive_ones(input_nums3), expected_output4 == max_consecutive_ones(input_nums4) )

print(max_consecutive_ones_test())

#Submit
class Solution(object):
  def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_count =0
    count = 0
    prev = 0

    if nums == [1]:
      return 1

    for i in range(0, len(nums)):
      if nums[i]==1:

        if prev==1:
          count=count+1

        else:
          count = 1
        prev = 1

      else:
        prev= 0 

      if count> max_count:
        max_count = count

    return max_count


