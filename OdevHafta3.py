# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:28:12 2022

@author: MehmetCanDuru

@lesson: DataScience
@instructor: MehmetAliCengiz
@issue: writing codes in lecture notes
"""

print("Merhaba veri bilimi")

print("merhaba\nveri\nbilimi")

print(55)
print(123456789+1)

exampleFloatNumber = 55.03 # Example Float Number
print(exampleFloatNumber)
print(type(exampleFloatNumber))

print(type(55+3j)) # Example Complex Number

print(type(True)) # Example Boolean data type 

#Example collection 
print(7+5)
#Example extraction
print(117-34)
#Example divide
print(45/4)
#Exampleimpact
print(3*4)
#Examples other operators
print(3**4)
print(30//4)
print(10%3)

exampleNumber = 35
print(type(exampleNumber))
print(type(str(exampleNumber)))  #type casting "int to str"

exampleStrNumber = "123"
print(type(exampleStrNumber))
print(type(int(exampleStrNumber)))  #type casting "str to int"

print(len(exampleStrNumber)) #string lengt


x = -2019
print(abs(x)) #absolute value

d= -3.54632
print(int(d)) #type casting

notes = [21,34,57,75,81,83,98,65]
print(len(notes)) #list lengt

#basics functions
def plus(a,b):
    return a+b

print(plus(3,7))

def func(x):
    return x*x+5

print(func(3))

def func2(x,y,z):
    return x**2+y**3+z**-2

print(func2(3,5,7))

def average(x):
    total_x = sum(x)
    len_x = len(x)
    return total_x / len_x

print(average([1,5,6,7,8,45,67]))

#example range func and loop

for i in range(10):
    print(i)

#example practice

def harmonicMean(s):
    n = len(s)
    totalNumbers = [1/s[i] for i in range(0,n)]
    harmonic_mean = n/sum(totalNumbers)
    return harmonic_mean

print(harmonicMean([1,5,6,7,8,45,67]))

#comparison operators

print(22 > 23)
print(22 < 23)
print(22 >= 23)
print(22 <= 23)
print(22 == 23)
print(22 != 23)

#example Dataframe and I/O

import pandas as pd
import numpy as np

data = pd.read_csv("BigmacPrice.csv")
print(data.head())
print(data.shape)

print(data.columns)

print(data.head(6))
print(data.tail(3))

print(data.describe())

#print(data.describe(include=['O'])
    









