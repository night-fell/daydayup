# -*- coding:utf-8 -*-
__author__ = "huohuo"

def insert_data(data_list):
    lenght = len(data_list)

    for i in range(1,lenght):
        key = data_list[i]
        j = i - 1
        while j >= 0:
            if data_list[j] > key:
                data_list[j + 1] = data_list[j]
                data_list[j] = key
            j = j - 1

    return data_list

def insert_sort(data_list):
    lenght = len(data_list)

    for i in range(1,lenght):
        key = data_list[i]
        j = i-1
        while j >= 0:
            if data_list[j] > key:
                data_list[j + 1] = data_list[j]
                data_list[j] = key
            j = j - 1

    return data_list

def charu_data(data_list):
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



