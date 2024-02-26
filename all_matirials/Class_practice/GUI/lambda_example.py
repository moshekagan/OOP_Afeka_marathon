l1 = [
    [2, 'Pini'],
    [7, 'mor'],
    [3, 'aviv'],
    [5, 'eitan']
]

def stam(x):
    return x[1]

print(l1)
print('after sorting', sorted(l1, key=stam))
print('after sorting', sorted(l1, key=lambda p: p[1]))


