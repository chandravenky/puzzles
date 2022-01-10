#Normal solution
def add_digits(input_number):

  res = input_number
  
  while len(str(res))> 1:

    current_number = str(res)

    res = 0
    
    for digit in str(current_number):

      res = res + int(digit)

  return res

#With recursion
def add_digits_recursively(input_number):

  res = 0
    
  for digit in str(input_number):

    res = res + int(digit)
  
  if len(str(res)) > 1:

    return add_digits_recursively(res)
    
  return res

#Best solution
def add_digits2(input_number):
  
  if input_number==0:
    return 0

  return input_number%9 or 9

# Tests
def add_digits_test():

  input_number1 = 11
  input_number2 = 38
  input_number3 = 0
  input_number4 = 36
  input_number5 = 37


  expected_output1 = 2
  expected_output2 = 2
  expected_output3 = 0
  expected_output4 = 9
  expected_output5 = 1
  
  result_tuple1 = ( add_digits(input_number1) == expected_output1, add_digits(input_number2) == expected_output2, add_digits(input_number3) == expected_output3, add_digits(input_number4) == expected_output4, add_digits(input_number5) == expected_output5)

  result_tuple2 = ( add_digits_recursively(input_number1) == expected_output1, add_digits_recursively(input_number2) == expected_output2, add_digits_recursively(input_number3) == expected_output3, add_digits_recursively(input_number4) == expected_output4, add_digits_recursively(input_number5) == expected_output5 )

  result_tuple3 = ( add_digits2(input_number1) == expected_output1, add_digits2(input_number2) == expected_output2, add_digits2(input_number3) == expected_output3, add_digits2(input_number4) == expected_output4, add_digits2(input_number5) == expected_output5 )

  return result_tuple1, result_tuple2, result_tuple3

print(add_digits_test())

#Leetcode
#Normal solution
class Solution(object):
    def addDigits(self, input_number):
        res = 0

        for digit in str(input_number):

            res = res + int(digit)

        if len(str(res)) > 1:

            return self.addDigits(res)

        return res

#Recursion
class Solution(object):
    def addDigits(self, input_number):
        res = 0

        for digit in str(input_number):

            res = res + int(digit)

        if len(str(res)) > 1:

            return self.addDigits(res)

        return res

#Best solution
class Solution(object):
    def addDigits(self, input_number):
  
        if input_number==0:
            return 0

        return input_number%9 or 9
