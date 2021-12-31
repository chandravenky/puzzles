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

#Tests
def merge_sorted_array_test():

  actual_output1 = merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3)
  actual_output2 = merge_sorted_array([1], 1, [], 0)
  actual_output3 = merge_sorted_array([0], 0, [1], 1)
  actual_output4 = merge_sorted_array([2,0], 1, [1], 1)
  actual_output5 = merge_sorted_array([1,2,3,0,0,0], 3, [4,5,6], 3)
  actual_output6 = merge_sorted_array([4,5,6,0,0,0], 3, [1,2,3], 3)
  actual_output7 = merge_sorted_array([1,2,3,4,5], 5, [], 0)

  expected_output1 = [1,2,2,3,5,6]
  expected_output2 = [1]
  expected_output3 = [1]
  expected_output4 = [1,2]
  expected_output5 = [1,2,3,4,5,6]
  expected_output6 = [1,2,3,4,5,6]
  expected_output7 = [1,2,3,4,5]

  return actual_output1 == expected_output1, actual_output2 == expected_output2, actual_output3 == expected_output3, actual_output4 == expected_output4, actual_output5 == expected_output5, actual_output6 == expected_output6, actual_output7 == expected_output7 

print(merge_sorted_array_test())

#For leetcode
class Solution(object):
    def merge(self, nums1, m, nums2, n):

        holding_pointer1 = m-1
        holding_pointer2 = n-1

        if m == 0:
            nums1[:] = nums2[:n]
        
        elif n ==0:
            pass
            
        else:

            for i in range(len(nums1)-1, 0, -1):

                if nums1[holding_pointer1] <= nums2[holding_pointer2]:

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
