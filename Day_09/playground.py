def add(*args):
    summing = 0
    for n in args:
        summing += n
    return summing


print(add(2, 5, 99, 34, 45))
