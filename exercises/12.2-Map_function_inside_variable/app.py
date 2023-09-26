names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name 
#Your code go here:
new_list=[]
for x in names:
    new_list.append(prepender(x))
print(new_list)
