my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list=[]
for a in range(len(my_list)):
    if type(my_list[a]) == dict or type(my_list[a]) == list:
        new_list.append(my_list[a])
print(new_list)

