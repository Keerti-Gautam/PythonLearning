# Use "def" to create new functions
""" The syntax for definition is
        def func_name(argument1, argument2, ...):
            statements to be executed

    These functions can be called by writing the function names.
"""

def add(x, y):
    # Can use print "x is {0} and y is {1}".format(x, y), print "Addition is", x+y
    return x+y  # Return values with a return statement

# Calling functions with parameters
print add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
print add(y=6, x=5)  # Keyword arguments can arrive in any order.
