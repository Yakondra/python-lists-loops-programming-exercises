arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odds(arr):
    result=0
    for i in arr:
        if i % 2 != 0:
            result += i
    return result
print(sum_odds(arr))