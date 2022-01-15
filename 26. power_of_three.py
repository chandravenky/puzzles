#Solution1
def power_of_three(input_number):

  if input_number<0:
    return False

  if input_number ==0 or input_number ==2:
    return False

  while input_number>3:

    input_number = input_number/3
    remainder = input_number % 3

    if remainder>0:
      return False

  return True

#Tests
def power_of_three_test():

  input_num1 = 27
  input_num2 = 0
  input_num3 = 9
  input_num4 = 25
  input_num5 = 1
  input_num6 = 19684
  input_num7 = -3
  input_num8 = 6
  
  expected_output1 = True
  expected_output2 = False
  expected_output3 = True
  expected_output4 = False
  expected_output5 = True
  expected_output6 = False
  expected_output7 = False
  expected_output8 = False

  return ( expected_output1 == power_of_three(input_num1), expected_output2 == power_of_three(input_num2), expected_output3 == power_of_three(input_num3), expected_output4 == power_of_three(input_num4), expected_output5 == power_of_three(input_num5), expected_output6 == power_of_three(input_num6), expected_output7 == power_of_three(input_num7), expected_output8 == power_of_three(input_num8) )

print(power_of_three_test())

#Leetcode
class Solution(object):
  def isPowerOfThree(self, input_number):
    """
    :type n: int
    :rtype: bool
    """
    if input_number<0:
      return False

    if input_number ==0 or input_number ==2:
      return False

    while input_number>3:
      #leetcode evaluates in Python 2.7
      input_number = float(input_number)/float(3)
      remainder = input_number % 3

      if remainder>0:
        return False

    return True
