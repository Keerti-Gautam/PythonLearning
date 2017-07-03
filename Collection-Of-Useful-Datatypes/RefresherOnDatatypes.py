# Dictionaries

filled_dict = {

        "one": 1,
        "two": 2,
        "three": 3
}

# Accessing values with keys
print filled_dict["one"]  # => 1
print filled_dict.keys()  # => ["three", "two", "one"] To get the keys
print filled_dict.values()  # => [3, 2, 1] To get the values
print filled_dict.items()  # => [("one", 1), ("two", 2), ("three", 3)] To get the values
# Use "get()" method to avoid the KeyError if key isn't present. The get method supports a default argument when the value is missing.
print filled_dict.get("four", 4)  # => 4

# lists

li = [1, 2, 3, 4, 5]
li.append(1) # Add stuff to the "end" of a list with append function append().
li.pop() # To remove an element from a list, use pop function pop(). Follows LIFO. Can put element to remove the specific element
li[0] # You can access a list like any you would access any array
print li[0:4:-2]  # =>[1, 3] # li[start:end:step]
other_li = [4, 5, 6]
new_list.extend(other_li)  # Concatenate lists with "extend()" function. List to be appended with is written inside parentheses.
print new_list # You can also add elements using extend() function like new_list.extend(["apples", "bananas"])
new_list.insert(1, 2)  # Insert an element at a specific index using insert(IndexWhereElementIsToBeInserted, NumberToInsertWith) function
print new_list.index(4)  # => 3 Get the index of the first item found using index(ElementWhoseIndexIsToBeFound)
new_list.remove(2)  # Remove first occurrence of a value with remove() function with the element to be removed inside parentheses.

# Sets

# Sets store sets (which are like lists but can contain no duplicates)
some_set = set([1, 2, 2, 3, 4, 5, 6])  # some_set is now set([1, 2, 3, 4])
filled_set = {1, 2, 2, 3, 4}  # => # Since Python 2.7, {} can be used to declare a set, here, {1, 2, 3, 4}
filled_set.add(5)  # # Add more items to a set. Filled_set is now {1, 2, 3, 4, 5}
print "intersection is: ", filled_set & some_set  # Do set intersection with &
print "union is: ", filled_set | some_set # Do set union with |

# Strings

print 'Hello!'+' World'
print 'Hello' ' World' #Can be added without the plus sign
print 'Hello'*4
print "That's what you wanted"[2] #returns the character on 2 index i.e. a
x = 'apple'
y = 'lemon'
z = "The items in the basket are %s and %s" % (x, y) # String formatting with %
# A newer way to format strings is the format method. This method is the preferred way
# Please note that %s or %d cannot be used with this format method and only braces are to be used.
print "{} is a {}".format("This", "placeholder")
print "{0} can be {1}".format("strings", "formatted")

# Tuples

# Tuples are like lists but are immutable or unchangeable.
tup = (1, 2, 3)
# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
d, e, f = 4, 5, 6  # you can leave out the parentheses
# Swapping two values! Easy shit, eh?
e, d = d, e  # d is now 5 and e is now 4
# Tuples are created by default if you leave out the parentheses
g = 4, 5, 6  # => (4, 5, 6)
# You can do all list thingies on tuples too!
