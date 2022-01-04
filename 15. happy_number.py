
def happy_number(input_num):

  def sum_square(digit):

    result =0

    for each_digit in str(digit):

      result = result + int(each_digit)**2

    return result
  
  square_sum = 0

  cycle_list = []

  while square_sum !=1:

    square_sum = sum_square(input_num)

    input_num = square_sum

    if input_num == 1:
      return True

    if input_num in cycle_list:
      return False

    else:
      cycle_list.append(input_num)

#Tests
def happy_number_test():

  input_number1= 19
  input_number2= 2
  input_number3= 12
  input_number4= 7
  input_number5= 1

  expected_output1= True
  expected_output2= False
  expected_output3= False
  expected_output4= True
  expected_output5= True

  return ( happy_number(input_number1) == expected_output1, happy_number(input_number2) == expected_output2, happy_number(input_number3) == expected_output3, happy_number(input_number4) == expected_output4, happy_number(input_number5) == expected_output5 )

print(happy_number_test())

#Leetcode Solution
class Solution(object):
  def isHappy(self, input_num):
    
    def sum_square(digit):

      result =0

      for each_digit in str(digit):

          result = result + int(each_digit)**2

      return result

    square_sum = 0
    
    cycle_list = []

    while square_sum !=1:

      square_sum = sum_square(input_num)

      input_num = square_sum
      
      if input_num == 1:
        return True
      
      if input_num in cycle_list:
        return False

      else:
        cycle_list.append(input_num)

    return False
