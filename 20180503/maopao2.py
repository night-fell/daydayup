# -*- coding:utf-8 -*-
__author__ = "huohuo"

import random

def generator():
    random_data = []
    for i in range(0,10):
        random_data.append(random.randint(1,1000))

    return random_data

def bubbles_sort(data_list):
    lenght = len(data_list)

    for i in range(0,lenght):
        for j in range(i + 1,lenght):
            if data_list[i] > data_list[j]:
                data_list[i],data_list[j] = data_list[j],data_list[i]

    return data_list

if __name__ == "__main__":
    print("冒泡2")

    random_data = generator()
    print(random_data)

    sorted_data = bubbles_sort(random_data)
    print(sorted_data)