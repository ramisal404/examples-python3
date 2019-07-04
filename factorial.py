"""
Recursion vs iteration implementation
"""

#Recursion
# runtime: Linear - O(N)
def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

#Iteration
def factorial(n):
  total = 1
  while n > 1:
    total = n * total
    n = n - 1
  return total
