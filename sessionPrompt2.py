#Session prompt 2

#Write a Python program that prints the sum of two floating point numbers, the difference between two integers, and the product of a floating point number and an integer. In each case, have the program print out the data type of the resulting answer.


import numpy as pip 

a = 2.84
b = 29.3
c = a + b

x = 50 
y = 21
z = x - y

e = a * x


print("a + b = " + str(c))
tc = type(c)
print(tc)

print("x - y = " + str(z))
tz = type(z)
print(tz)

print("a * x = " + str(e))
te = type(e)
print(te)