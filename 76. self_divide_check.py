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

def self_dividing_numbers_test():

  input_left1 = 1
  input_left2 = 47

  input_right1 = 22
  input_right2 = 85

  expected_output1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
  expected_output2 = [48, 55, 66, 77]

  return ( expected_output1 == self_dividing_numbers(input_left1, input_right1), expected_output2 == self_dividing_numbers(input_left2, input_right2) )

print(self_dividing_numbers_test())

class Solution(object):
    def self_divide_check(self, num):

        str_num = str(num)
        
        for num_string in str_num:
            
            num_int = int(num_string)
            
            # if num%num_int !=0:
            if num_int==0:
                return False
            
            if divmod(num, num_int)[1] !=0:
                return False
            
        return True        
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        
        for i in range(left, right+1):
            
            if self.self_divide_check(i):
                
                result.append(i)
                
        return result
    
