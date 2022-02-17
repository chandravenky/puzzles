
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
