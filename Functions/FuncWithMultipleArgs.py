# You can define functions that take a variable number of positional args, which will be interpreted as a tuple by using *
# Writing args and kwargs are not necessary, you can write var or vars and it would work the same

def varargs(*args):
    return args

print varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of keyword args as well, which will be interpreted as a dict by using **
def keyword_args(**kwargs):
    return kwargs


# Let's call it to see what happens
print keyword_args(big="foot", loch="ness", x=5)  # => {"big": "foot", "loch": "ness", "x": 5} note that here x is treated as a dict element with a key and a value

# You can do both at once too
def all_the_args(*args, **kwargs):
    print args
    print kwargs
    return kwargs #return args+kwargs Will show error as dict to tuple concatenation isn't possible.
    # Multiplication with two isn't possible with return statement as dict cannot be multiplied with int

print all_the_args(1, 2, a="lion", b=4) # prints
# All_the_args(a="lion", b=4, 1, 2) # Cannot do this because either all kwargs or args, and together the order of kwargs after args should be maintained.
# When calling functions, you can do the opposite of args/kwargs!

def all_these_args(*kwargs, **args):
    print args
    print kwargs

print all_these_args(1, 2, a="lion", b=4)

"""
def all_these_args(*args, **kwargs):
    print args
    print kwargs

print all_these_args(a="tiger", b="hey", 2, 3)
Doesn't work because keyword arguments cannot be followed by non keyword arguments
"""

# Use * to expand positional args and use ** to expand keyword args.
def all_such_args(*kwargs, **args):
    print args
    print kwargs
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_such_args(*args)  # equivalent to foo(1, 2, 3, 4)
all_such_args(**kwargs)  # equivalent to foo(a=3, b=4)
all_such_args(*args, **kwargs)  # equivalent to foo(1, 2, 3, 4, a=3, b=4)


# you can pass args and kwargs along to other functions that take args/kwargs by expanding them with * and ** respectively
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print varargs(*args)
    print keyword_args(**kwargs)

pass_all_the_args(200, 300, name="tom", pet="rat", food="pizza")
