#Solution1
def intersection(nums1, nums2):

  store = {}
  result_list = []

  for i in range(0, len(nums1)):

    if nums1[i] not in store:
      store[nums1[i]] = 1
    
    else:
      store[nums1[i]] = store[nums1[i]] + 1


  for i in range(0, len(nums2)):

    if nums2[i] in store:

      store[nums2[i]] = store[nums2[i]] -1
      
      result_list.append(nums2[i])

      if store[nums2[i]] == 0:
        del store[nums2[i]]


  return result_list

#Tests
def intersection_test():

  nums11, nums12 = [1,2,2,1], [2,2]
  nums21, nums22 = [4,9,5], [9,4,9,8,4]
  
  expected_output1 = [2,2]
  expected_output2 = [9,4]

  return ( expected_output1 == intersection(nums11, nums12), expected_output2 == intersection(nums21, nums22) )

print(intersection_test())

#Leetcode
class Solution(object):
  def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    store = {}
    result_list = []

    for i in range(0, len(nums1)):

      if nums1[i] not in store:
        store[nums1[i]] = 1

      else:
        store[nums1[i]] = store[nums1[i]] + 1


    for i in range(0, len(nums2)):

      if nums2[i] in store:

        store[nums2[i]] = store[nums2[i]] -1

        result_list.append(nums2[i])

        if store[nums2[i]] == 0:
          del store[nums2[i]]


    return result_list


