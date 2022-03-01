#Problem 383

def ransom_note(ransomNote, magazine):

  magazine_store = {}
        
  for i in range(0, len(magazine)):
      
    if magazine[i] not in magazine_store:
      magazine_store[magazine[i]] = 1
        
    else:
      magazine_store[magazine[i]] = magazine_store[magazine[i]] + 1
        
  for i in range(0, len(ransomNote)):
      
    if ransomNote[i] not in magazine_store:
      return False
      
    else:
      magazine_store[ransomNote[i]] = magazine_store[ransomNote[i]] - 1
          
      if magazine_store[ransomNote[i]] == 0:
        del magazine_store[ransomNote[i]]
              
  return True
  
#Add tests
def ransom_note_test():

  input_ransom1 = "a" 
  input_ransom2 = "aa"
  input_ransom3 = "aa"

  input_magazine1 = "b"
  input_magazine2 = "ab"
  input_magazine3 = "aab"

  expected_output1 = False
  expected_output2 = False
  expected_output3 = True

  return ( expected_output1 == ransom_note(input_ransom1, input_magazine1), expected_output2 == ransom_note(input_ransom2, input_magazine2), expected_output3 == ransom_note(input_ransom3, input_magazine3) )

print(ransom_note_test())

#Solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_store = {}
        
        for i in range(0, len(magazine)):
            
            if magazine[i] not in magazine_store:
                magazine_store[magazine[i]] = 1
                
            else:
                magazine_store[magazine[i]] = magazine_store[magazine[i]] + 1
                
        for i in range(0, len(ransomNote)):
            
            if ransomNote[i] not in magazine_store:
                return False
            
            else:
                magazine_store[ransomNote[i]] = magazine_store[ransomNote[i]] - 1
                
                if magazine_store[ransomNote[i]] == 0:
                    del magazine_store[ransomNote[i]]
                    
        return True
        
