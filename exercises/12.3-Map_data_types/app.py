list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
        return items
new_list= []
for x in range(len(list_Strings)):
        if type(list_Strings[x]) == int or type(list_Strings[x]) == str:
                new_list.append(type(list_Strings[x]))
        #new_list = list(map(type_list, list_Strings))
print(new_list)