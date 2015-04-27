#!/usr/bin/python3

# Probably useless, included just because
from collections import OrderedDict

# Used to one-line summing of list elements
from functools import reduce
from operator import add

# Used to create combination groups
from itertools import combinations

# Because I didn't feel like using argparse on a Sunday
import sys

def remove_existing(o_set, c_set):
    '''Identify and remove items from o_set that are within c_set.
    If a value within c_set is not found within o_set, return
    (False, None); else returns (True, (<Remaining values>)).'''
    
    success = True
    result = list(o_set)
    
    for value in c_set:
        if value in result:
            # At least one of value was found,
            # remove the first one.
            result.remove(value)
        else:
            # c_set contains values that don't
            # exist in o_set, fail
            success = False
            result = None
            break
    if success:
        # Stylistic choice
        result = tuple(result)
    
    return (success, result)

# Pull list of numbers from command line arguments
values = list(map(int, sys.argv[1:]))
# Make dict to hold all the results
results = OrderedDict()

# Handy holder
value_count = len(values)

# Build sets that allow for two sets to exist, down
# to minimum size of two. Length - 1 sets allow for
# all size 1 sets to be evaluated.
for set_size in range(value_count - 1, 1, -1):
    for v_set in combinations(values, set_size):
        # Save sets based on the sum of the values
        v_sum = reduce(add, v_set)
        if v_sum in results:
            results[v_sum].append(v_set)
        else:
            results[v_sum] = [v_set,]

# Cull sets for which there are only one set of values
# that adds to its sum.
candidates = {k: v for k, v in results.items() if len(v) > 1}

# Of the remaining sets,
for key, sets in candidates.items():
    # Choose pairs of sets,
    for u, v in combinations(sets, 2):
        # That combined are a subset of the original entry set
        success, cross_set = remove_existing(values, u)
        success, _         = remove_existing(cross_set, v)
        if success:
            print(key, u, v)
