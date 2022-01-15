#Solution1
def power_of_three(input_number):

  if input_number<0:
    return False

  if input_number ==0 or input_number ==2:
    return False

  while input_number>3:

    input_number = input_number/3
    remainder = input_number % 3

    if remainder>0:
      return False

  return True
