

def license_key_formatting(s, k):

  s = s.upper()
  s = list(s.replace("-", ""))
  s_reversed = s[::-1]


  output = ""
  for i in range(0, len(s_reversed), k):

    output = output + ''.join(s_reversed[i:i+k]) + '-'

  result = output[::-1]
  return result[1:]

#Tests
def license_key_formatting_test():

  input_license_key1 = "5F3Z-2e-9-w"
  input_license_key2 = "2-5g-3-J"

  input_k1 = 4
  input_k2 = 2

  expected_output1 = "5F3Z-2E9W"
  expected_output2 = "2-5G-3J"

  return ( expected_output1 == license_key_formatting(input_license_key1, input_k1), expected_output2 == license_key_formatting(input_license_key2, input_k2) )

print(license_key_formatting_test())

#Submit
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.upper()
        s = list(s.replace("-", ""))
        s_reversed = s[::-1]

        output = ""
        for i in range(0, len(s_reversed), k):

            output = output + ''.join(s_reversed[i:i+k]) + '-'


        result = output[::-1]
        return result[1:]
