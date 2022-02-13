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
