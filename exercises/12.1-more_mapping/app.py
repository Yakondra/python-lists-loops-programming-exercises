myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:
def incremente_by_one (x):
  new_list = x*3
  return new_list
result = list(map(incremente_by_one, myNumbers))  
print(result)