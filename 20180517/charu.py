# -*- coding:utf-8 -*-
__author__ = "huohuo"

import random

def generator():
    random_data = []
    for i in range(0,10):
        random_data.append(random.randint(1,1000))

    return random_data

def insert_sort(data_list):
    lenght = len(data_list)

    for i in range(1,lenght):
        key = data_list[i]
        j = i -1
        while j >= 0:
            if data_list[j] > key:
                data_list[j + 1] = data_list[j]
                data_list[j] = key
            j = j - 1

    return data_list

if __name__ == "__main__":
    print("复习插入")

    random_data = generator()
    print(random_data)

    sorted_data = insert_sort(random_data)
    print(sorted_data)

