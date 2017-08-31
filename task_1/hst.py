import math


def get_hist(data, length, beans_num):
    X = []
    Y = []
    for i in range(beans_num):
        Y.append(0)
    ext_val = get_min_max(data)
    diapason = ext_val['max_val'] - ext_val['min_val']
    interval_size = diapason/beans_num

    for i in range(beans_num):
        X.append(ext_val['min_val'] + interval_size*i)

    X.append(max(ext_val['max_val'], ext_val['min_val'] + interval_size*beans_num))

    for i in range(length):
        idx = math.floor((data[i] - ext_val['min_val'])/interval_size)
        if idx == beans_num:
            idx -= 1
        Y[idx] += 1
    return {'x_val': X, 'y_val': Y, 'int_size': interval_size}


def get_min_max(data):
    min_val = min(data)
    max_val = max(data)

    return {'min_val': min_val, 'max_val': max_val}


# if bins not equally distributed
"""def bin_binary_search(el, array):
    last_idx = len(array) - 1

    curr_low = 0
    curr_up = len(array) - 1
    curr_idx = len(array)//2

    while 0 < curr_idx < last_idx and not(array[curr_idx - 1] <= el < array[curr_idx]):
        if el >= array[curr_idx]:
            curr_low = curr_idx + 1
        else:
            curr_up = curr_idx
        curr_idx = (curr_up + curr_low)//2

    return curr_idx - 1"""
