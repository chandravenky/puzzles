#Solution1
def ugly_number(input_number):

  if input_number ==0:
    return False

  while input_number!=1:

    for i in [2,3,5]:

      if input_number%i ==0:
        
        input_number = input_number/i

        break

        # print(input_number, i)
      
    else:

      return False

  return True

# Tests
def ugly_number_test():

  input_number1 = 6
  input_number2 = 1
  input_number3 = 14
  input_number4 = 8
  input_number5 = 0


  expected_output1 = True
  expected_output2 = True
  expected_output3 = False
  expected_output4 = True
  expected_output5 = False


  return ugly_number(input_number1) == expected_output1, ugly_number(input_number2) == expected_output2, ugly_number(input_number3) == expected_output3, ugly_number(input_number4) == expected_output4, ugly_number(input_number5) == expected_output5

print(ugly_number_test())
#Leetcode
class Solution(object):
  def isUgly(self, input_number):
    """
    :type n: int
    :rtype: bool
    """
    
    if input_number ==0:
      return False

    while input_number!=1:

      for i in [2,3,5]:

        if input_number%i ==0:

          input_number = input_number/i

          break

                
        else:

          return False

    return True

