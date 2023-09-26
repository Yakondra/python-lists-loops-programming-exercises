import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  person["name"] , people))
birth_list = list(map(lambda person:  calculateAge(person["birthDate"]) , people))

chan=[]
for name, age in zip(name_list, birth_list):
    plas = (name, age)
    perro="Hello, my name is "+str(plas[0])+" and I am "+str(plas[1])+" years old"
    chan.append(perro)
print(chan)

#print("Hello, my name is "+str(name_list)+" and I am "+str(birth_list)+" years old\n")
