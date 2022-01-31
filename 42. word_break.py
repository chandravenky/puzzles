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
