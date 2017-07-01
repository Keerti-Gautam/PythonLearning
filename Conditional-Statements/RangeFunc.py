# coding: utf-8

# The above statement was written because somewhere in the code there was a hidden character which wa a non ASCII character for which encoding wasn't declared.

# "range(number)" returns a list of numbers from zero to the given number
# The format for range is "range(lower, upper, steps_of_incrementation)""
# Putting a lower, upper or steps of incrementation is optional. If only a number n is provided, it'll return from 0 till that n-1.

# Simple iteration
for i in range(4):
    print i

# range(lower, upper) returns a list of numbers from the lower number to the upper number
for i in range(4, 8):
    print i

# Range(lower, upper, incrementation)

for i in range(0, -100, -20):
    print i

# Using len() and range() function together
tiny_story = ['Mary', 'had', 'a', 'little', 'lamb', 'which', 'was', 'not', 'so', 'little']
for j in range(len(tiny_story)): # Made a tiny mistake here which I corrected. I was trying to iterate j in len(tiny_story) or 10 which makes no fucking sense.
    print (j, tiny_story[j])

# In some ways the object returned by range func behaves as if it was a list but in fact, it is not.
# It is an object which returns the successive items of the desired sequence (i.e. the sequence we want to be printed or returned) when you iterate over it, but it doesn’t really make the list, thus saving space.
print range(20)
print "This produces a list because still using Python 2.x"
# We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.
# We have seen that the for statement is such an iterator.

# The function list() is another; it creates lists from iterables:
list (range(15))
