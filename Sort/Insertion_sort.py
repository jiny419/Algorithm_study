#!/usr/bin/env python
# coding: utf-8

# # Insertion sort



A = [12, 11, 13, 5, 6]

def insertion_sort(arr) :
    for i in range(len(arr)) :
        min_idx = i
        for j in range(i, len(arr)) :
            if arr[min_idx] > arr[j] :
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        


insertion_sort(A)

for i in range(len(A)) :
    print(A[i])







