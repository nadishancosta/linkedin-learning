def powered(base_num,pow_num):
    total=base_num
    for index in range(pow_num-1):
        total = total * base_num
    return total

print(powered(2,3))