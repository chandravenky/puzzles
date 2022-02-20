#Problem 409

def longest_palindrome(s):

  store = {}
  
  for i in range(0, len(s)):
      
    if s[i] not in store:
      store[s[i]] = 1
    
    else:
      store[s[i]] = store[s[i]] + 1
        
  pair_characters_store = {key: value for key, value in store.items() if value>=2}
  
  len_palindrome_pair_list = [int(value/2) for value in pair_characters_store.values()]
  
  extra_char_in_pair = [value for value in pair_characters_store.values() if value%2!=0]
  
  tot_character = sum(len_palindrome_pair_list)
  
  extra_char = 1 if len(store) > len(pair_characters_store) or len(extra_char_in_pair)>0 else 0
  
  return tot_character*2 + extra_char
        
  
#Add tests
def longest_palindrome_test():

  input_s1 = "abccccdd" 
  input_s2 = "a"
  input_s3 = "bb"

  expected_output1 = 7
  expected_output2 = 1
  expected_output3 = 2

  return ( expected_output1 == longest_palindrome(input_s1), expected_output2 == longest_palindrome(input_s2), expected_output3 == longest_palindrome(input_s3) )

print(longest_palindrome_test())

#Solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        store = {}
        
        for i in range(0, len(s)):
            
            if s[i] not in store:
                store[s[i]] = 1
            
            else:
                store[s[i]] = store[s[i]] + 1
                
        pair_characters_store = {key: value for key, value in store.items() if value>=2}
        
        len_palindrome_pair_list = [int(value/2) for value in pair_characters_store.values()]
        
        extra_char_in_pair = [value for value in pair_characters_store.values() if value%2!=0]
        
        tot_character = sum(len_palindrome_pair_list)
        
        extra_char = 1 if len(store) > len(pair_characters_store) or len(extra_char_in_pair)>0 else 0
        
        return tot_character*2 + extra_char
        
        
