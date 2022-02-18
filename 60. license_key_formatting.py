def license_key_formatting(s, k):

  s = s.upper()
  s = list(s.replace("-", ""))
  s_reversed = s[::-1]


  output = ""
  for i in range(0, len(s_reversed), k):

    output = output + ''.join(s_reversed[i:i+k]) + '-'

  result = output[::-1]
  return result[1:]
