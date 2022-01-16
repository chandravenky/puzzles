#Solution1
def power_of_four(input_number):

  if input_number==1 or input_number==4:
    return True

  if input_number<0 or input_number<4:
    return False

  while input_number>4:

    input_number = input_number/4
    remainder = input_number % 4

    if remainder>0:
      return False

  return True

#Tests
def power_of_four_test():

  input_num1 = 16
  input_num2 = 0
  input_num3 = 5
  input_num4 = 1
  input_num5 = -4
  
  expected_output1 = True
  expected_output2 = False
  expected_output3 = False
  expected_output4 = True
  expected_output5 = False

  return ( expected_output1 == power_of_four(input_num1), expected_output2 == power_of_four(input_num2), expected_output3 == power_of_four(input_num3), expected_output4 == power_of_four(input_num4), expected_output5 == power_of_four(input_num5) )

print(power_of_four_test())

#Leetcode
class Solution(object):
  def isPowerOfFour(self, input_number):
    """
    :type n: int
    :rtype: bool
    """
    if input_number==1 or input_number==4:
      return True

    if input_number<0 or input_number<4:
      return False

    while input_number>4:

      input_number = float(input_number)/float(4)
      remainder = input_number % 4

      if remainder>0:
        return False

    return True
