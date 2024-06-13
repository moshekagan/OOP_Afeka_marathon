# 1 2 3 4 5 6.......
# 1 1 2 3

def fibo(index):
    if index == 1:
        return 1
    if index == 2:
        return 1
    if index > 2:
        prev_1 = fibo(index-1)
        prev_2 = fibo(index-2)
        return prev_1 + prev_2


print(fibo(1)) # 1
print(fibo(2)) # 1
print(fibo(3)) # 2
print(fibo(4)) # 3
print(fibo(10)) # 55
print(fibo(8)) # 21
print(fibo(9)) # 34

