def num_different_integers(s):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    s = s + "x"
    num_list = list("0123456789")
    str_current = ""
    store = {}
    
    for i in range(0, len(s)):

      if s[i] not in num_list:
        if len(str_current)>0:
          store[str_current] = 1

          str_current = ""
        
        else:
          pass

      else:
        if s[i] != "0":
          str_current = str_current + s[i]

        else:
          if len(str_current)>0:
            str_current = str_current + s[i]
          
          else:
            if i+1<len(s):
              if s[i+1] not in num_list:
                str_current = str_current + s[i]
            
            else:
              pass

    if len(str_current)>0:
      store[str_current] = 1

    return len(store.keys())

#Solution 2 - Better solution
def num_different_integers2(s):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i=0
    num_list = list("0123456789")
    store = {}
    str_current = ""
    
    while i < len(s):
      
      if s[i] not in num_list:
        i = i+1

      else:
        j=i
        while j<len(s) and s[j] in num_list:
          
          str_current = str_current + s[j]
          j = j+1
          
        store[str_current] = 1
        str_current = ""
        i=j

    nums = [int(item) for item in store.keys()]
    return len(set(nums))
