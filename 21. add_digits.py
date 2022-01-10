#Normal solution
def add_digits(input_number):

  res = input_number
  
  while len(str(res))> 1:

    current_number = str(res)

    res = 0
    
    for digit in str(current_number):

      res = res + int(digit)

  return res
