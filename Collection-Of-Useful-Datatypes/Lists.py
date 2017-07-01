# Lists store sequences. List is like an array. Indexes start with 0

# You can start with a pre-filled list
other_li = [4, 5, 6]

# An empty list can be appended at the end with numbers
li = []

# Add stuff to the "end" of a list with append function append(). YYes only end.
# The data to be appended with should be written inside parentheses

li.append(1)  # li is now [1]
li.append(2)  # li is now [1, 2]
li.append(4)  # li is now [1, 2, 4]
li.append(3)  # li is now [1, 2, 4, 3]
li.append(8)


print li

# To remove an element from a list, use pop function pop(). Follows LIFO
# pop operation removes element from the "end" of the list if used without any index in function parentheses
li.pop()  # => 3 and li is now [1, 2, 4, 3]
print li

li.pop(2) # Trying to remove data from element 2
print li # Yes Happens!

# Let's put it back
li.append('b')  # Only append(b) can't be used because b is assumed to be a variable which isn't defined.
print li
b = "Here"
li.pop()
print li
li.append(b) # Now doesn't show any error
print li

# You can access a list like any you would access any array
li[0]  # => 1
print li[0]
print li[2]

# Assign new values to indexes that have already been initialized with =
li[0] = 42 #set a new value at index 1
print li  # => 42

li[0] = 1  # Note: setting it back to the original value
print li

# You can visualise the list from R to L by taking negative indexes from the rightmost element.
print li[-2]  # => 3

# Looking out of bounds is an IndexError
#li[5]  # Raises an IndexError as no value is assigned to index 4.

# Ranges can be looked at with slice syntax (the lower index is included while upper isn't). It's a closed/open range.
print li[1:3]  # => [2, 3]
# Omit the beginning
print li[2:]  # => [3, 'Here']
# Omit the end
print li[:3]  # => [1, 2, 3]

# Select every second entry
print li[::2]  # =>[1, 3]

# Reverse a copy of the list
print li[::-1]  # => ['Here', 3, 2, 1]

# Use any combination of these to make advanced slices
# li[start:end:step]
print li[0:4:2]  # =>[1, 3]

# Remove elements from a list with "del"
del li[2]  # li is now [1, 2, 'Here']
print li
# You can add lists
new_list = li + other_li  # => [1, 2, 'Here', 4, 5, 6]
print new_list

# Concatenate lists with "extend()" function. List to be appended with is written inside parentheses.
new_list.extend(other_li)  # Now li is [1, 2, 'Here', 4, 5, 6, 4, 5, 6]
print new_list
# You can also add elements using extend()
new_list.extend(["apples", "bananas"])
print new_list

# Remove first occurrence of a value with remove() function with the element to be removed inside parentheses.
new_list.remove(2)  # li is now [1, 'Here', 4, 5, 6, 4, 5, 6]
print new_list
#new_list.remove(2)  # Raises a ValueError as 2 is not in the list anymore
#print new_list

# Insert an element at a specific index using insert(IndexWhereElementIsToBeInserted, NumberToInsertWith) function
new_list.insert(1, 2)  # li is now [1, 2, 'Here', 4, 5, 6, 4, 5, 6] again
print new_list

# Get the index of the first item found using index(ElementWhoseIndexIsToBeFound)
print new_list.index(4)  # => 3
print new_list
#print new_list.index(10)  # Raises a ValueError as 7 is not in the list
#print new_list

# Check for existence in a list with "in"
if 1 in new_list:
    print "Yay"
else:
    print "No"  # => Yep

# Examine the length with "len()"
print len(li)  # => 6
print len(new_list)
