def isomorphic(s, t):

  if len(s)!=len(t):
    return False
  
  store = {}
  for i in range(0, len(t)):
    if s[i] not in store:
      store[s[i]] = t[i]
          
    else:
      if store[s[i]] == t[i]:
          pass
      else:
          return False
  
  #Check for dups
  if len(store.values()) != len(set(store.values())):
    return False
          
  return True

#Tests
def isomorphic_test():

  input_string1a, input_string1b  = "egg", "add"
  input_string2a, input_string2b = "foo", "bar"
  input_string3a, input_string3b = "paper", "title"

  expected_result1 = True
  expected_result2 = False
  expected_result3 = True

  return isomorphic(input_string1a, input_string1b) == expected_result1, isomorphic(input_string2a, input_string2b) == expected_result2, isomorphic(input_string3a, input_string3b) == expected_result3
