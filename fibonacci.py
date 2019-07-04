"""
Recursion vs iteration implementation
"""

#Recursion
# runtime: Exponential - O(2^N)

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

#Iteration
def fibonacci(n):
  fibs = [0, 1]
  
  if n <= len(fibs) - 1:
    return fibs[n]
  
  while n > len(fibs) - 1:
    fibs.append(fibs[-1]+fibs[-2])
  return fibs[-1]
