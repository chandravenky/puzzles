#Problem 728

def self_divide_check(num):

  str_num = str(num)
  
  for num_string in str_num:
    
    num_int = int(num_string)
    
    if num_int==0:
      return False
    if divmod(num, num_int)[1] !=0:
      return False
      
  return True    
