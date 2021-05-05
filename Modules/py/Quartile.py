#!/usr/bin/env python
# coding: utf-8

# Quartile class to calculate quartile features

import numpy as np

class Quartile:
    def __init__(self, nodes):
        self.nodes = nodes
        self.first_q = np.quantile(nodes, .25, interpolation='midpoint')
        self.second_q = np.quantile(nodes, .50, interpolation='midpoint')
        self.third_q = np.quantile(nodes, .75, interpolation='midpoint')
 
    def calc_quartiles(self):
        first_q, second_q, third_q, fourth_q = [], [], [], []

        for node in self.nodes:
            if node <= self.first_q:
                first_q.append(1)
                second_q.append(0)
                third_q.append(0)
                fourth_q.append(0)
            elif node <= self.second_q:
                first_q.append(0)
                second_q.append(1)
                third_q.append(0)
                fourth_q.append(0)
            elif node <= self.third_q:
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



