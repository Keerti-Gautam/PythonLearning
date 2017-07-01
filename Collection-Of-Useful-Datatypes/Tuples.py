# Tuples are like lists but are immutable or unchangeable.
tup = (1, 2, 3)
print tup[0]  # => 1

#tup[0] = 3  # Raises a TypeError because elements cannot be changed. 'Tuple' object doesn't allow item assignment
print tup

# You can do all list thingies on tuples too
print len(tup)  # => 3

new_tup = tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
print new_tup

print new_tup[:2]  # => (1, 2)

2 in new_tup  # => True

# You can unpack tuples (or lists) into variables
print "You can unpack tuples (or lists) into variables. Woah! You could do that!"
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
d, e, f = 4, 5, 6  # you can leave out the parentheses
print a, b, c, d, e, f

# Swapping two values! Easy shit, eh?
e, d = d, e  # d is now 5 and e is now 4
print d, e

# Tuples are created by default if you leave out the parentheses
g = 4, 5, 6  # => (4, 5, 6)
print g
