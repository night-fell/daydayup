# -*- coding:utf-8 -*-
__author__ = "huohuo"

import random

def generator():
    random_data = []
    for i in range(1,10):
        random_data.append(random.randint(1,1000))

    return random_data
