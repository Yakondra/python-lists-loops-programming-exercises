Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
        res=x*1.8+32
        return res
result = list(map(fahrenheit_values, Celsius_values))
print(result)
#(0 °C × 9 / 5) + 32 = 32 °F
