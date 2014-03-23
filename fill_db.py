#coding: utf-8

from html_lib import sqler
import random

listnames= ["Crimean", "Alaska", "Some other unclassified territory", "MIG-25", "MIG-31", "Learjet-23","Learjet-45", "Learjet-60","Mi-8","Floating point"]

start, end = 6,16
for i in xrange(start,end):
    sqler.add_row(i, listnames[start-i], int(random.random() * 100000) )


