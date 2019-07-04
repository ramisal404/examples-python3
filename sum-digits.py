"""
Recursive and iterative approach
"""
#Iterative
# Linear - O(N)
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

#Iterative
def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n//10) + last_digit
