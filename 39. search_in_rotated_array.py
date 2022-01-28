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

def search_test():

  input_array1, input_target1 = [4,5,6,7,0,1,2], 0
  input_array2, input_target2 = [4,5,6,7,0,1,2], 3
  input_array3, input_target3 = [1], 0
  input_array4, input_target4 = [1], 1
  input_array5, input_target5 = [2,0], 0
  input_array6, input_target6 = [1,3], 1
  input_array7, input_target7 = [3,5,1], 3

  expected_output1= 4
  expected_output2= -1
  expected_output3= -1
  expected_output4= 0
  expected_output5= 1
  expected_output6= 0
  expected_output7= 0

  result_tuple = ( expected_output1 == search(input_array1, input_target1), expected_output2 == search(input_array2, input_target2), expected_output3 == search(input_array3, input_target3), expected_output4 == search(input_array4, input_target4), expected_output5 == search(input_array5, input_target5), expected_output6 == search(input_array6, input_target6), expected_output7 == search(input_array7, input_target7) )

  return result_tuple

print(search_test())

#Leetcode
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

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
