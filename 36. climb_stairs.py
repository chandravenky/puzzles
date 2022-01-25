def climb_stairs(n):

  ways=[0, 1,2,3]

  if n<=3:
    return n

  for i in range(3, n):

    ways.append(ways[-1] + ways[-2])

  return ways[-1]

#Tests
def climb_stairs_test():

  input_num1= 2
  input_num2=3
  input_num3= 4
  input_num4= 5

  expected_output1= 2
  expected_output2= 3
  expected_output3= 5
  expected_output4= 8

  result_tuple = ( expected_output1 == climb_stairs(input_num1), expected_output2 == climb_stairs(input_num2), expected_output3 == climb_stairs(input_num3), expected_output4 == climb_stairs(input_num4) )

  return result_tuple

print(climb_stairs_test())

#Leetcode
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways=[0, 1,2,3]

        if n<=3:
            return n

        for i in range(3, n):

            ways.append(ways[-1] + ways[-2])

        print(i, ways)
        return ways[-1]
