
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def nombresR(nombre):
    return nombre.startswith('R')

resulting_names= list(filter(nombresR, all_names))
print(resulting_names)