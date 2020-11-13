#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file
Self-contained Python program for benchmarking sorting algorithms.

SOMETIMES IT WORKS

Original code for the sorting functions available at:

http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python/
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

Copyright for the "main" code: Nuno Fachada, 2017, MIT License
http://opensource.org/licenses/MIT
"""

# No
# More
# Code

import random
import sys

# This is the function
# that implements Bubble Sort
# As we know, this is the most efficient sorting algorithm
# known to man

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap!

def selection_sort(items):
    """ Implementation of selection sort """
    for fillslot in range(len(items) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if items[location] > items[positionOfMax]:
                positionOfMax = location

        temp = items[fillslot]
        items[fillslot] = items[positionOfMax]
        items[positionOfMax] = temp
            
def merge_sort(items):
    """ Implementation of mergesort """
    if len(items) > 1:
 
        mid = len(items) // 2    # Determine the midpoint and split
        left = items[0:mid]
        right = items[mid:]
 
        merge_sort(left)        # Sort left list in-place
        merge_sort(right)       # Sort right list in-place
 
        l, r = 0, 0
        for i in range(len(items)):     # Merging the left and right list
 
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None
 
            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')

def quick_sort(items):
    """ Implementation of quick sort """
    if len(items) > 1:
        pivot_index = len(items) // 2
        smaller_items = []
        larger_items = []
 
        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)
 
        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items
 
if __name__ == "__main__":

    # Require three or four arguments
    if (len(sys.argv) < 4) or (len(sys.argv) > 5):
        print("python sorttest.py SORTALG NUM SEED [CHECK]")
        print("    SORTALG - Sorting algorithm: bubble, selection, merge, quick")
        print("        NUM - Number of elements to sort")
        print("       SEED - Seed for random number generator")
        print("      CHECK - Check if sorting is correct")
        sys.exit(-1)
        
    # Select sorting algorithm
    algs = {'bubble'    : bubble_sort,
            'selection' : selection_sort,
            'merge'     : merge_sort,
            'quick'     : quick_sort}

    if sys.argv[1] in algs:
        sortfun = algs[sys.argv[1]]
    else:
        raise Exception("Unknown algorithm '%s'" % sys.argv[1])

    # Number of elements to sort and seed
    numels = int(sys.argv[2])
    seed = int(sys.argv[3])
    
    # Generate random number list to perform sorting
    random.seed(seed)
    list2sort = [random.randint(0, 2 ** 31 - 1) for _ in range(numels)]
    
    # Perform sorting    
    sortfun(list2sort)
    
    # Check sorting?
    if len(sys.argv) == 5:
        if sorted(list2sort) == list2sort:
            print("Sorting Ok!")
        else:
            print("Sorting did not work!")
            sys.exit(-1)
