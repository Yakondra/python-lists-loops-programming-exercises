all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(all_colors):
    colorin = list(filter(lambda hot: hot["sexy"], all_colors))
    return colorin 

def generate_li(color):
    color= 
    
chi=[]
for label in all_colors:
    chi=set("<li>"+str(filter_colors(label))+"</li>")
    
print(chi)
    
# def calculateAge(birthDate):
#     today = datetime.date.today()
#     age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
#     return age

# name_list = list(map(lambda person:  person["name"] , people))
# birth_list = list(map(lambda person:  calculateAge(person["birthDate"]) , people))

# chan=[]
# for name, age in zip(name_list, birth_list):
#     plas = (name, age)
#     perro="Hello, my name is "+str(plas[0])+" and I am "+str(plas[1])+" years old"
#     chan.append(perro)
# print(chan)

# noloiso = list(filter(lambda tarea: tarea["done"], tasks))
# loiso=[]
# for tarea in noloiso:
#     loiso.append(tarea)
# print(loiso)