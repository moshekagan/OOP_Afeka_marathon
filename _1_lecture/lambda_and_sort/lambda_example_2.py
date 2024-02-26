# Example 2: Sorting a list of tuples

grads_list = [(1, 5), (4, 2), (2, 3), (7, 8)]
# [(4, 2), (2, 3), (1, 5), (7, 8)]

sorted_list = sorted(grads_list, key=lambda item: item[1])
print(sorted_list)
