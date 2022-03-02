#Problem 599

def find_restaurant(list1, list2):

  store = {}
  min_sum = 99999999
  result= []
  
  for i in range(0, len(list1)):
      
    store[list1[i]] = i
      
  for i in range(0, len(list2)):
      
    if list2[i] in store:
      sum_total = store[list2[i]] + i
      if sum_total == min_sum:
        result.append(list2[i])
          
      if sum_total< min_sum:
        min_sum = sum_total
        result = [list2[i]]
            
  return result
