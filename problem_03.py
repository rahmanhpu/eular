#!/usr/bin/env python

"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def get_dividers(n):
	i = 1
	dividers = []
	while i < n:
		if n%i == 0:
			dividers.append(i)
			n = n/i
			i=i+1
		else:
			i=i+1
	dividers.append(n)
	return dividers

print(get_dividers(13195))

print(get_dividers(600851475143)[-1])



#n=600851475143
#n=13195
#i=2
#while i<n:
#    if(n%i)==0:
#        n=n/i
#        i=i
#    else:
#        i=i+1
#print(i)
