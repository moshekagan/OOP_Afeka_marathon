# n! = 1 * 2 * 3 * ... n
# 0! = Error
# 1! = 1
# 2! = 1 * 2 = 1! * 2
# 3! = 1 * 2 * 3 = 2! * 3
# 89! = 88! * 89


def fact(num):
    if num == 1:
        return 1

    num_fact = fact(num-1) * num
    return num_fact

print(fact(1)) # 1
print(fact(2)) # 2
print(fact(3))
print(fact(89))


