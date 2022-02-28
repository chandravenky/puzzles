#Problem 605

def can_place_mismatch(flowerbed, n):

  i = 0
  
  while i<len(flowerbed):
    
    if flowerbed[i] == 0:
      
      if i == len(flowerbed)-1:
        n=n-1
        break
      elif flowerbed[i+1] == 0:
        n = n-1
        i= i+2
      else:
        i=i+3
    
    else:
      i = i+2
          
  return n<=0

#Add tests
def can_place_mismatch_test():

  input_flowerbed1 = [1,0,0,0,1]
  input_flowerbed2 = [1,0,0,0,1]
  input_flowerbed3 = [1,0,0,0,1,0,0]
  input_flowerbed4 = [0,0,1,0,0]

  input_n1 = 1
  input_n2 = 2
  input_n3 = 2
  input_n4 = 1

  expected_output1 = True
  expected_output2 = False
  expected_output3 = True
  expected_output4 = True

  return ( expected_output1 == can_place_mismatch(input_flowerbed1, input_n1), expected_output2 == can_place_mismatch(input_flowerbed2, input_n2), expected_output3 == can_place_mismatch(input_flowerbed3, input_n3), expected_output4 == can_place_mismatch(input_flowerbed4, input_n4) )

print(can_place_mismatch_test())a
