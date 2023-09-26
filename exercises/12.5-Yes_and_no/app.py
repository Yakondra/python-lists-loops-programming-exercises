theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def evol(theBools):
    if theBools == 0:
        return "woko"
    else:
        return "wiki"

bul = list(map(evol,theBools))
print(bul)


    