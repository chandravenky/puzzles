#Solution1
def power_of_two(input_number):

  if input_number == 1 or input_number ==2:
    return True
  
  if input_number == 0:
    return False

  while input_number>=2:

    input_number = input_number/2

    if input_number ==2:

      return True

  return False

# Tests
def power_of_two_test():

  input_number1 = 1
  input_number2 = 16
  input_number3 = 17
  input_number4 = 0
  input_number5 = 2

  return ( power_of_two(input_number1) == True, power_of_two(input_number2) == True, power_of_two(input_number3) == False, power_of_two(input_number4) == False, power_of_two(input_number5) == True )

print(power_of_two_test())

#Leetcode
class Solution(object):
  def isPowerOfTwo(self, input_number):
    """
    :type n: int
    :rtype: bool
    """
    if input_number == 1 or input_number==2:
      return True

    if input_number == 0:
      return False

    while input_number>=2:

      #leetcode evaluates in Python 2.7
      input_number = float(input_number)/float(2)

      if input_number ==2:

        return True

    return False
