
#Easy solution
def reverse_integer(x):

  x_string = str(abs(x))

  reversed_x_string = x_string[::-1]

  reversed_x_int = int(reversed_x_string)

  if reversed_x_int> (2**31 +1) or reversed_x_int < -2**31:
    return 0

  if x<0:
    return -reversed_x_int

  return reversed_x_int

#Arithmetic
def reverse_integer2(x):

  output = 0

  abs_x =abs(x)
  
  while abs_x >=1:

    remainder= abs_x%10

    output = output*10 + remainder

    abs_x = abs_x//10

  if x<0:
    output = -output

  if output> (2**31 +1) or output < -2**31:
    return 0

  return output

#Tests
def reverse_integer_test():

  input_num1 = 123
  input_num2 = -123
  input_num3 = 120
  input_num4 = 9463847412
  input_num5 = 2563847412
  input_num6 = -2563847412

  expected_output1 = 321
  expected_output2 = -321
  expected_output3 = 21
  expected_output4 = 2147483649
  expected_output5 = 0
  expected_output6 = 0

  return ( expected_output1 == reverse_integer(input_num1), expected_output2 == reverse_integer(input_num2), expected_output3 == reverse_integer(input_num3), expected_output4 == reverse_integer(input_num4), expected_output5 == reverse_integer(input_num5),
  expected_output6 == reverse_integer(input_num6), 

  expected_output1 == reverse_integer(input_num1), expected_output2 == reverse_integer(input_num2), expected_output3 == reverse_integer(input_num3), expected_output4 == reverse_integer(input_num4), expected_output5 == reverse_integer(input_num5),
  expected_output6 == reverse_integer(input_num6) )

print(reverse_integer_test())
