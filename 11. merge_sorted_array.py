#Solution1
def merge_sorted_array(nums1, m, nums2, n):

  holding_pointer1 = m-1
  holding_pointer2 = n-1

  if m == 0:
    return nums2

  if n ==0:
    pass
  
  for i in range(len(nums1)-1, 0, -1):

    # print(i, nums1, nums2, holding_pointer1, holding_pointer2)
    if holding_pointer2<0:
      break

    elif nums1[holding_pointer1] <= nums2[holding_pointer2]:

      nums1[i] = nums2[holding_pointer2]
      
      holding_pointer2 = holding_pointer2 -1

      if holding_pointer2<0:

        break

    
    else:
      nums1[i] = nums1[holding_pointer1]

      holding_pointer1 = holding_pointer1 - 1

      if holding_pointer1<0:

        nums1[:holding_pointer2+1]= nums2[:holding_pointer2+1]
        break


  return nums1
