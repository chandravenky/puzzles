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
