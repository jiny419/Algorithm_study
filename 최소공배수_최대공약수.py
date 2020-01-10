#!/usr/bin/env python
# coding: utf-8

# ### 최소공배수 최대공약수
# 

a, b = map(int, input().split())



def checking(a, b) :
    if a>=b :
        return a, b
    else :
        return b, a




def gcd(a, b) :
    n1, n2 = checking(a,b)
    temp = n2
    n2 = n1%n2
    n1 = temp
    
    return n1


def lcm(a, b):
    return int(a*b/gcd(a, b))



gcd(a, b)


lcm(a,b)






