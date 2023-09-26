incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# #Your code go here:
def data_transformer(incoming_ajax_data):
    name_list = list(map(lambda name:  name["name"] , incoming_ajax_data))
    lastname_list = list(map(lambda name:  name["last_name"] , incoming_ajax_data))

    chan=[]
    for name, lastname in zip(name_list, lastname_list):
        plas = (name, lastname)
        chan.append(plas[0]+" "+plas[1])
    return chan

print(data_transformer(incoming_ajax_data))

#new_list=list(map(data_transformer,))
# name_list = list(map(lambda person:  person["name"] , people))
# birth_list = list(map(lambda person:  calculateAge(person["birthDate"]) , people))
