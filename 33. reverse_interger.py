
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
