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
