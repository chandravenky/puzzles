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
        
  
#Add tests
def find_restaurant_test():

  input_list1a = ["Shogun","Tapioca Express","Burger King","KFC"]
  input_list2a = ["Shogun","Tapioca Express","Burger King","KFC"]
  input_list3a = ["Shogun","Tapioca Express","Burger King","KFC"]

  input_list1b = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
  input_list2b = ["Shogun"]
  input_list3b = ["KFC","Shogun","Burger King"]
  

  expected_output1 = ["Shogun"]
  expected_output2 = ["Shogun"]
  expected_output3 = ["Shogun"]

  return ( expected_output1 == find_restaurant(input_list1a, input_list1b), expected_output2 == find_restaurant(input_list2a, input_list2b), expected_output3 == find_restaurant(input_list3a, input_list3b) )

print(find_restaurant_test())

#Solution
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
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
            
        
        
        
