#if can be used as an expression
# Equivalent of C's ternary operator '?:'
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

# If Else Conditional Statement. Indentation is significant in python!
""" if (condition):
      statements
    elif (condition):
      statements
    else:
      statements
  """

# Example

some_var = 5

if some_var > 10:
    print "some_var is totally bigger than 10."
elif some_var < 10:  # This elif clause is optional.
    print "some_var is smaller than 10."
else:  # This is optional too.
    print "some_var is indeed 10."


number = raw_input("Input the times the value to be compared to 30: ")
if number > 30:
    print "Number is greater"
    print "consider changing to lower number"
elif number < 30:
    print "Number is less than 30"
else:
    print "Number is equal."
