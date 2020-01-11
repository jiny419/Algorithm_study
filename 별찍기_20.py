#!/usr/bin/env python
# coding: utf-8

# # 별찍기 - 20


def print_star(a) :
    i=1
    while(i<=a) :
        if i%2!=0 :
            print("* "*a)
        else :
            print(" *"*a)
        i+=1


a = int(input())

print_star(a)

