#Your code go here:
yey=[]
x = 20
while x > 0:
    if x % 5 == 0:
        yey.append(str(x) + '!')
    else:
        yey.append(str(x))
    x -= 1
yey.append("LIFTOFF")
print(yey)
