#Problem 507

def perfect_number(num):

  divisor_sum = 1

  if num == 1:
    return False
  
  for i in range(2, int(num**0.5)):

    if num%i == 0:
      divisor_sum = divisor_sum + i + num/i

  if divisor_sum == num:
    return True

  return False
