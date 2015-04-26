#!/usr/bin/python3

from collections import OrderedDict
from functools import reduce
from itertools import combinations
from operator import add
import sys

def remove_existing(o_set, c_set):
    success = True
    result = list(o_set)
    for value in c_set:
        if value in result:
            result.remove(value)
        else:
            success = False
            result = None
            break
    if success:
        result = tuple(result)
    
    return (success, result)

values = list(map(int, sys.argv[1:]))
results = OrderedDict()

value_count = len(values)

for set_size in range(value_count - 1, 1, -1):
    for v_set in combinations(values, set_size):
        v_sum = reduce(add, v_set)
        if v_sum in results:
            results[v_sum].append(v_set)
        else:
            results[v_sum] = [v_set,]

candidates = {k: v for k, v in results.items() if len(v) > 1}

for key, sets in candidates.items():
    for u, v in combinations(sets, 2):
        success, cross_set = remove_existing(values, u)
        success, _         = remove_existing(cross_set, v)
        if success:
            print(key, u, v)
