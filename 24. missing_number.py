#Solution1
def missing_number(input_array):

  superset_list = list(range(0,len(input_array)+1))
  # print(superset_list)

  return list(set(superset_list)-set(input_array))[0]

#Best solution with O(1) space
def missing_number2(input_array):
    """
    :type nums: List[int]
    :rtype: int
    """

    tot_sum = (len(input_array)*(len(input_array) + 1))/2
    
    for i in input_array:
        
        tot_sum = tot_sum -i
        
    return tot_sum

#Tests
def missing_number_test():

  input_array1 = [9,6,4,2,3,5,7,0,1]
  input_array2 = [0,1,3]
  input_array3 = [0,1]


  expected_output1 = 8
  expected_output2 = 2
  expected_output3 = 2

  result_tuple1 = ( expected_output1 == missing_number(input_array1), expected_output2 == missing_number(input_array2), expected_output3 == missing_number(input_array3) )

  result_tuple2 = ( expected_output1 == missing_number2(input_array1), expected_output2 == missing_number2(input_array2), expected_output3 == missing_number2(input_array3) )

  return result_tuple1, result_tuple2

print(missing_number_test())

#Leetcode
class Solution(object):
  def missingNumber(self, input_array):
    """
    :type nums: List[int]
    :rtype: int
    """

    tot_sum = (len(input_array)*(len(input_array) + 1))/2
    
    for i in input_array:
        
      tot_sum = tot_sum -i
        
    return tot_sum

