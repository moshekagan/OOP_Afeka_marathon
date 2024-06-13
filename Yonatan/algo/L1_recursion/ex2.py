# f(x) = x*2
# f(2) = 4
# f(5) = 10
#
# g(x) = if x > 1 : g(x-1) + 2
#        else 1
#
# g(2) = g(2-1) + 2 = g(1) + 2 = 1 + 2 = 3

# n = 5
# res = 1+2+3+4+5 = 15

def sum_num(num):
    sum = 0
    for i in range(1, num+1): # i =  1, 2, 3, 4, 5
       sum = sum + i
    return sum


print(sum_num(5))

# num = 3 -> 6
# num = 2 -> 3
# num = 1 -> 1
# num = 0 -> 0
def sum_num_rec(num):
    if num == 0:
        return 0

    prev_sum_num = sum_num_rec(num-1)
    return prev_sum_num + num


print(sum_num_rec(0))
print(sum_num_rec(1))
print(sum_num_rec(5))
print(sum_num_rec(100))
