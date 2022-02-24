#Problem 520



def detect_capital(word):
  
  if len(word) == 1:
    return True
        
  #first_capital
  if word[0].isupper():
    first_capital = 1
  else:
    first_capital = 0
  
  #second_capital
  if word[1].isupper():
    second_capital = 1
  else:
    second_capital = 0
      
  if first_capital == 0 and second_capital==1:
    return False
  
  for i in range(2, len(word)):
    if first_capital == 1 and second_capital == 1:
      if word[i].islower():
        return False
          
    if first_capital == 1 and second_capital == 0:
      if word[i].isupper():
        return False
          
    if first_capital ==0:
      if word[i].isupper():
        return False
          
  return True

#Tests
def detect_capital_test():

  input_nums1 = "USA"
  input_nums2 = "FlaG"
  input_nums3 = "mL"
  input_nums4 = "cVe"

  expected_output1 = True
  expected_output2 = False
  expected_output3 = False
  expected_output4 = False

  return ( expected_output1 == detect_capital(input_nums1), expected_output2 == detect_capital(input_nums2), expected_output3 == detect_capital(input_nums3), expected_output4 == detect_capital(input_nums4))

print(detect_capital_test())

#Submit
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        
        #first_capital
        if word[0].isupper():
            first_capital = 1
        else:
            first_capital = 0
        
        #second_capital
        if word[1].isupper():
            second_capital = 1
        else:
            second_capital = 0
            
        if first_capital == 0 and second_capital==1:
            return False
        
        for i in range(2, len(word)):
            if first_capital == 1 and second_capital == 1:
                if word[i].islower():
                    return False
                
            if first_capital == 1 and second_capital == 0:
                if word[i].isupper():
                    return False
                
            if first_capital ==0:
                if word[i].isupper():
                    return False
                
        return True
