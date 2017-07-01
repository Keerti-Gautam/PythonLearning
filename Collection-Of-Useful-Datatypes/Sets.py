# Sets store sets (which are like lists but can contain no duplicates)
empty_set = set()

# Initialize a "set()" with a bunch of values
some_set = set([1, 2, 2, 3, 4])  # some_set is now set([1, 2, 3, 4])
print some_set
print "Set cannot have duplicates!!"

# order is not guaranteed, even though it may sometimes look sorted
another_set = set([4, 9, 3, 2, 2, 1])  # another_set is now set([9, 2, 3, 4, 1])
print another_set

# Since Python 2.7, {} can be used to declare a set
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}
print "Hooray! No more two brackets now!"

# Add more items to a set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
print filled_set

# Do set intersection with &
other_set = {3, 4, 5, 6}
print other_set

print "intersection is: ", filled_set & other_set  # => {3, 4, 5}

# Do set union with |
print "union is: ", filled_set | other_set  # => {1, 2, 3, 4, 5, 6, 9}

# Do set difference with -
x = {1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
print "Set difference is: ", x

# Do set symmetric difference with ^
y = {1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
print "Symmetric difference: ", y

# Check if set on the left is a superset of set on the right
if ({1, 2} >= {1, 2, 3}):
    print "Yay"
else:
    print "Nay"  # => False

# Check if set on the left is a subset of set on the right
if ({1, 2} <= {1, 2, 3}):
    print "yep"
else:
    print "nay"  # => True

# Check for existence in a set with in
if 2 in filled_set:
    print "hi"
else:
    print "no"  # => True
if 10 in filled_set:
    print "Yep there"
else:
    print "no"  # => False
