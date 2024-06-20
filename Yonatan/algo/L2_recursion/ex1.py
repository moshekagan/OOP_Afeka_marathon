# כתבו פונקציה רקורסיבית המקבלת מספר ומחזירה את מספר הספרות .הזוגיות

# 123 -> 1
# 121212 -> 3

def count_evens(num):
    if num == 0:
        return 0

    last_digit = num % 10

    new_num = num // 10
    count = count_evens(new_num)

    if last_digit % 2 == 0: # its even
        return count + 1
    else: # is odd
        return count


print(count_evens(1)) # 0
print(count_evens(2)) # 1
print(count_evens(12)) # 1
print(count_evens(346)) # 2
print(count_evens(123123123123))










# print(count_evens(0)) # 1


