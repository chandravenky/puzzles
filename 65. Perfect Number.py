#Problem 507

def perfect_number(num):

  divisor_sum = 1

  if num == 1:
    return False
  
  for i in range(2, int(num**0.5)):

    if num%i == 0:
      divisor_sum = divisor_sum + i + num/i

  if divisor_sum == num:
    return True

  return False

#Tests
def perfect_number_test():

  input_nums1 = 28
  input_nums2 = 7
  input_nums3 = 99999991
  input_nums4 = 1

  expected_output1 = True
  expected_output2 = False
  expected_output3 = False
  expected_output4 = False

  return ( expected_output1 == perfect_number(input_nums1), expected_output2 == perfect_number(input_nums2), expected_output3 == perfect_number(input_nums3), expected_output4 == perfect_number(input_nums4))

print(perfect_number_test())

#Submit
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divisor_sum = 1
        
        if num == 1:
            return False

        for i in range(2, int(num**0.5) + 1):

            if num%i == 0:
                divisor_sum = divisor_sum + i + num/i

        if divisor_sum == num:
            return True

        return False
