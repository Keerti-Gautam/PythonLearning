# Function Scope
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = 20  # => 43
    return x+num  # => 43

def set_global_x(num):
    global x
    print x  # => 5
    x = num  # global var x is now set to 6
    print x  # => 6


print set_x(43)
set_global_x(6)
