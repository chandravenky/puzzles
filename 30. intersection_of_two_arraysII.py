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
