def contains_pattern(arr, m, k):

  pattern = {}

  for i in range(0, len(arr)):

    if arr[i:i+m] == arr[i+m:i+2*m]:
      
      pattern_string = ''.join(str(v) for v in arr[i:i+m])

      if pattern_string in pattern and pattern_string:
        
        pattern[pattern_string] = pattern[pattern_string] + 1
      
      else:
        pattern[pattern_string] = 2

    else:
      pattern = { key:value for key, value in pattern.items() if value>=k}

  #filter for results
  result =  { key:value for key, value in pattern.items() if value>=k}

  if result:
    return True
  
  return False
