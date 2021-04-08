#!/usr/bin/env python
# coding: utf-8

import numpy as np

 
def calc_quartiles(nodes, num_of_nodes):
    first_q, second_q, third_q, fourth_q = [], [], [], []

    for node in nodes:
        if node <= np.quantile(nodes, .25, interpolation='midpoint'):
            first_q.append(1)
            second_q.append(0)
            third_q.append(0)
            fourth_q.append(0)
        elif node <= np.quantile(nodes, .50, interpolation='midpoint'):
            first_q.append(0)
            second_q.append(1)
            third_q.append(0)
            fourth_q.append(0)
        elif node <= np.quantile(nodes, .75, interpolation='midpoint'):
            first_q.append(0)
            second_q.append(0)
            third_q.append(1)
            fourth_q.append(0)
        else:
            first_q.append(0)
            second_q.append(0)
            third_q.append(0)
            fourth_q.append(1)

    return first_q, second_q, third_q, fourth_q



