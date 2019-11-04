#!/usr/bin/env python

"""
Problem 4:


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


"""
       
import time

print("please put your number")
value=input()
num_input=int(value)
start_time = time.time()
num = 0
for num1 in range(num_input,0,-1):
    for num2 in range(num1,0,-1):
        num3=num1*num2
        if num3>num:
            s = str(num1*num2)
            if s[::1] == s[::-1]:
                num=num3

print("your palindromic sequence is ", num)
print("--- %s seconds ---" % (time.time() - start_time))

