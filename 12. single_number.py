#Solution1
def single_number(input_array):

  unique_track = {}

  for i in range(0,len(input_array)):
  

    if input_array[i] in list(unique_track.keys()):

      del unique_track[input_array[i]]
    
    else:
      unique_track[input_array[i]] = 1

  return list(unique_track.keys())[0]

#Solution 2
def single_number_2(input_array):

  res = input_array[0]

  for i in range(1, len(input_array)):

    #print(res, bin(res), input_array[i], bin(input_array[i]))

    res ^= input_array[i] #bitwise XOR

    #print("result", res, bin(res))

  return res

#Tests
def single_number_test():

  input_array1 = [2,2,1]
  input_array2 = [4,1,2,1,2]
  input_array3 = [1]

  return single_number(input_array1) == 1, single_number(input_array2) == 4, single_number(input_array3) == 1

def single_number_2_test():

  input_array1 = [2,2,1]
  input_array2 = [4,1,2,1,2]
  input_array3 = [1]

  return single_number_2(input_array1) == 1, single_number_2(input_array2) == 4, single_number_2(input_array3) == 1

print(single_number_test())
print(single_number_2_test())

#For Leetcode
#Solution1
class Solution(object):
    def singleNumber(self, input_array):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_track = {}

        for i in range(0,len(input_array)):

            if input_array[i] in unique_track:

                del unique_track[input_array[i]]

            else:
                unique_track[input_array[i]] = 1

        return list(unique_track.keys())[0]

#Solution2
class Solution(object):
    def singleNumber(self, input_array):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = input_array[0]

        for i in range(1, len(input_array)):

            #print(res, bin(res), input_array[i], bin(input_array[i]))

            res ^= input_array[i] #bitwise XOR

            #print("result", res, bin(res))

        return res
