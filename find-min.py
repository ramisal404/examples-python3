"""
Iterative and Recursive approach
"""

#Iterative
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min
  
#Recursive
def find_min(my_list, min = None):
  if not my_list:
    return min

  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min(my_list[1:], min)
