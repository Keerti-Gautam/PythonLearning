# Python has a print statement
print "I'm Python. Nice to meet you!"  # => I'm Python. Nice to meet you!

# Simple way to get input data from console
input_string_var = raw_input( "Enter some data: ")  # Returns the data as a string
input_var = input("Enter some data: ")  # Evaluates the data as python code or converts input as if it were python code
# Warning: Caution is recommended for input() method usage
# Note: In python 3, input() is deprecated and raw_input() is renamed to input() meaning they both will return the data as strings.

# To change the data into an integer you can use x = int(raw_input("Enter some data here: "))

def addition():
    x = int(raw_input("Please enter the first number to be added: "))
    y = int(raw_input("Please enter the second number to be added: "))
    return x+y

print addition()
