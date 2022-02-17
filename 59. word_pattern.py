
def word_pattern(pattern, s):

  patterns_list = list(pattern)
  s_list =  s.split(" ")
  
  if len(patterns_list)!=len(s_list):
    return False
  
  store = {}
  for i in range(0, len(patterns_list)):
      
    if pattern[i] not in store:
      store[pattern[i]] = s_list[i]

          
    else:
      if store[pattern[i]] == s_list[i]:
        pass
      else:
        return False
          
  if len(store) != len(set(store.values())):
    return False
  
  return True

#Test
def word_pattern_test():

  input_pattern1 = "abba"
  input_pattern2 = "abba"
  input_pattern3 = "aaaa"
  input_pattern4 = "abba"

  input_s1 = "dog cat cat dog"
  input_s2 = "dog cat cat fish"
  input_s3 = "dog cat cat dog"
  input_s4 = "dog dog dog dog"

  expected_output1 = True
  expected_output2 = False
  expected_output3 = False
  expected_output4 = False

  return ( expected_output1 == word_pattern(input_pattern1, input_s1), expected_output2 == word_pattern(input_pattern2, input_s2), expected_output3 == word_pattern(input_pattern3, input_s3), expected_output4 == word_pattern(input_pattern4, input_s4) )

print(word_pattern_test())

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        
        patterns_list = list(pattern)
        s_list =  s.split(" ")
        
        if len(patterns_list)!=len(s_list):
            return False
        
        store = {}
        for i in range(0, len(patterns_list)):
            
            if pattern[i] not in store:
                store[pattern[i]] = s_list[i]

                
            else:
                if store[pattern[i]] == s_list[i]:
                    pass
                else:
                    return False
                
        if len(store) != len(set(store.values())):
            return False
        
        return True
            
        
