#Solution
def two_out_of_three(nums1, nums2, nums3):

  stored_master = {}
  stored_1 = {}
  stored_2 = {}
  stored_3 = {}

  for i in range(0, len(nums1)):
    
    if nums1[i] not in stored_1:
      stored_1[nums1[i]] = 1
      stored_master[nums1[i]] = 1

    else:
      pass
  
  for i in range(0, len(nums2)):
    
    if nums2[i] not in stored_master:
      stored_2[nums2[i]] = 1
      stored_master[nums2[i]] = 1

    else:
      if nums2[i] not in stored_2: 
        stored_master[nums2[i]] = 2
  
  for i in range(0, len(nums3)):
    
    if nums3[i] not in stored_master:
      stored_3[nums3[i]] = 1
      stored_master[nums3[i]] = 1

    else:
      if nums3[i] not in stored_3:
        stored_master[nums3[i]] = 2
  

  final_list = { key: value for key, value in stored_master.items() if value>1 }
      
  return list(final_list.keys())


#Tests
def two_out_of_three_test():

  return ( two_out_of_three([1,1,3,2],[2,3], [3]) == [3,2], 
  two_out_of_three([3,1], [2,3], [1,2]) == [3,1, 2], 
  two_out_of_three([1,2,2], [4,3,3], [5]) == [],)

print(two_out_of_three_test())

#Leetcode
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        stored_master = {}
        stored_1 = {}
        stored_2 = {}
        stored_3 = {}

        for i in range(0, len(nums1)):

            if nums1[i] not in stored_1:
                stored_1[nums1[i]] = 1
                stored_master[nums1[i]] = 1

            else:
                pass

        for i in range(0, len(nums2)):

            if nums2[i] not in stored_master:
                stored_2[nums2[i]] = 1
                stored_master[nums2[i]] = 1

            else:
                if nums2[i] not in stored_2: 
                    stored_master[nums2[i]] = 2

        for i in range(0, len(nums3)):

            if nums3[i] not in stored_master:
                stored_3[nums3[i]] = 1
                stored_master[nums3[i]] = 1

            else:
                if nums3[i] not in stored_3:
                    stored_master[nums3[i]] = 2


        final_list = { key: value for key, value in stored_master.items() if value>1 }

        return list(final_list.keys())

