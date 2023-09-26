arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
print(arr)
new_list=[]
for flop in range(len(arr) - 1, -1, -1):
   new_list.append(arr[flop])
print(new_list)
