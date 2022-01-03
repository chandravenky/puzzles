#Solution1
def majority_element(nums):

  threshold = len(nums)/2
  cnt_dict = {}

  if len(nums) == 1:
    return nums[0]

  for num in nums:

    if num in cnt_dict:
      cnt_dict[num] = cnt_dict[num] + 1
      if cnt_dict[num]>=threshold:
        return num

    else:
      cnt_dict[num] = 1

#Better solution with O(1) solution

#Boyer-Moore algorithm
def majority_element_2(nums):

  count = 0
  res = nums[0]

  for num in nums[1:]:

    if num != res:
      
      count = count-1
      
      if count <0:
        count = 0
        res = num
    
    else:
      count = count + 1

  return res

#Tests
def majority_element_test():

  input_array1= [1]
  input_array2 = [3,2,3]
  input_array3= [2,2,1,1,1,2,2]

  expected_output1= 1
  expected_output2= 3
  expected_output3= 2

  result_tuple1 = ( majority_element(input_array1) == expected_output1, majority_element(input_array2) == expected_output2, majority_element(input_array3) == expected_output3 )

  result_tuple2 = ( majority_element_2(input_array1) == expected_output1, majority_element_2(input_array2) == expected_output2, majority_element_2(input_array3) == expected_output3 )

  return result_tuple1, result_tuple2


print(majority_element_test())

#Leetcode
#Solution1
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        threshold = len(nums)/2

        cnt_dict = {}
        
        if len(nums) == 1:
            return nums[0]

        for num in nums:

            if num in cnt_dict:
                cnt_dict[num] = cnt_dict[num] + 1
                if cnt_dict[num]>threshold:
                    return num

            else:
                cnt_dict[num] = 1

#Solution2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = nums[0]

        for num in nums[1:]:

            if num != res:

                count = count-1

                if count <0:
                    count = 0
                    res = num

            else:
                count = count + 1

        return res
