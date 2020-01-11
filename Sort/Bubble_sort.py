#!/usr/bin/env python
# coding: utf-8

# # Bubble sort



A = [11, 12, 22, 25, 34, 64, 90]

def bubble_sort(arr) :
    n = len(arr) 
    
    for i in range(n) :
        for j in range(0, n-i-1) :
            if(arr[j] > arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]




bubble_sort(A)

for i in range(len(A)) :
    print(A[i])





