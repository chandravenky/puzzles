#Solution1
def reverse_string(input_string_array):

  traverse_length = len(input_string_array)//2
  
  for i in range(0, traverse_length):
    
    holding_pointer = input_string_array[i]

    input_string_array[i] = input_string_array[len(input_string_array) -1 - i]

    input_string_array[len(input_string_array) -1 - i] = holding_pointer

  return input_string_array


#Tests
def reverse_string_test():

  input_string_array1 = ["h","e","l","l","o"]
  input_string_array2 = ["H","a","n","n","a","h"]
  
  expected_output1 = ["o","l","l","e","h"]
  expected_output2 = ["h","a","n","n","a","H"]

  return ( expected_output1 == reverse_string(input_string_array1), expected_output2 == reverse_string(input_string_array2) )

print(reverse_string_test())

#Leetcode
class Solution(object):
  def reverseString(self, input_string_array):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    traverse_length = len(input_string_array)//2

    for i in range(0, traverse_length):

      holding_pointer = input_string_array[i]

      input_string_array[i] = input_string_array[len(input_string_array) -1 - i]

      input_string_array[len(input_string_array) -1 - i] = holding_pointer

    return input_string_array

