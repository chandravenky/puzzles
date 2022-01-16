#Solution1
def power_of_four(input_number):

  if input_number==1 or input_number==4:
    return True

  if input_number<0 or input_number<4:
    return False

  while input_number>4:

    input_number = input_number/4
    remainder = input_number % 4

    if remainder>0:
      return False

  return True
