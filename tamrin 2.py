lst = [2,5,8,12,9,-25,4,102]

def count_evens(lst):
    counter = 0
    for i in lst:
        if i % 2 == 0:
            counter += 1
    return counter

print("count of evens : ", count_evens(lst))