def word_break2(s, word_dict):
  """
  :type s: str
  :type goal: str
  :rtype: bool
  """
  dp = []
        
  for i in range(0, len(s)):
    # print(i, s[:i+1] , dp)
    if s[:i+1] in word_dict:
      dp.append(i+1)
        
    else:
      
      for j in dp:
        
        if s[j:i+1] in word_dict:
          
          dp.append(i+1)

       
  if len(s) in dp:
      return True
  
  return False

#12:30 a working solution by 12:45
#Tests
def word_break2_test():

  input_s1 = "leetcode"
  input_s2 = "applepenapple"
  input_s3 = "catsandog"

  input_word_dict1 = ["leet","code"]
  input_word_dict2 = ["apple","pen"]
  input_word_dict3 = ["cats","dog","sand","and","cat"]

  expected_output1 = True
  expected_output2 = True
  expected_output3 = False

  actual_output1 = word_break2(input_s1, input_word_dict1)
  actual_output2 = word_break2(input_s2, input_word_dict2)
  actual_output3 = word_break2(input_s3, input_word_dict3)

  return ( expected_output1 == actual_output1, expected_output2 == actual_output2, expected_output3 == actual_output3 )

print(word_break2_test())
