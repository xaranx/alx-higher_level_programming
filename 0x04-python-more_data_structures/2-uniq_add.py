#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = set()
    sum = 0
    for num in my_list:
        if num not in unique_num:
            unique_num.add(num)
            sum += num
    return sum
