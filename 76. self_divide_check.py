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

def self_dividing_numbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    result=[]
    
    for i in range(left, right+1):
        
      if self_divide_check(i):
          
        result.append(i)
            
    return result
