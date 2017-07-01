# None is just a value that commonly is used to signify 'empty', or 'no value here'.

#None is an object
None  # => None

#The equality '==' symbol should never be used to compare objects to None. Should use 'is' instead
"etc" is None  # => False
None is None  # => True
"etc" is not None # => True

# The 'is' operator tests for object identity (compares types of objects). This isn't very useful when dealing with primitive values (i.e. only numeric values or strings), but is very useful when dealing with objects.

# Any object can be used in a Boolean context and considered truthy or falsey if they return true or false respectively.

# The following values are considered falsey (bool() function on them returns False):
#    - None
#    - zero of any numeric type (e.g., 0, 0L, 0.0, 0j)
#    - empty sequences (e.g., '', (), [])
#    - empty containers (e.g., {}, set())
#    - instances of user-defined classes meeting certain conditions
#      see: https://docs.python.org/2/reference/datamodel.html#object.__nonzero__

# All other values are truthy (bool() function on them returns True):

print "Examples of values considered falsey"
bool(0)  # => False
bool("")  # => False
bool([])  # => False
bool(None)  # => False
