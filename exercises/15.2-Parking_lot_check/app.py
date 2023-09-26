parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(parking_state):
    available_slots= 0
    occupied_slots= 0
    state={}
    for fila in parking_state:
      for valor in fila:
        if valor == 1:
          occupied_slots += 1
        elif valor == 2:
          available_slots += 1
    state["total_slots"]= available_slots+occupied_slots
    state["available_slots"]=available_slots
    state["occupied_slots"]= occupied_slots
    return state
print(get_parking_lot(parking_state))            
            
            
# total_slots: 6,
# available_slots: 1,
# occupied_slots: 5