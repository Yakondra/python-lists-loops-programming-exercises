people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_people=[]
    for x in people:
        if x == person_name:
           continue
        else:
            new_people.append(x)
    return new_people
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))