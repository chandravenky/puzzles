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
