# String formatting with %
#Even though the % string operator will be deprecated on Python 3.1 and removed later at some time, it may still be good to know how it works.
x = 'apple'
y = 'lemon'
z = "The items in the basket are %s and %s" % (x, y)

print z

print "%s is used for strings and %d is used for integer values"

# A newer way to format strings is the format method. This method is the preferred way
# Please note that %s or %d cannot be used with this format method and only braces are to be used.
print "{} is a {}".format("This", "placeholder")
print "{0} can be {1}".format("strings", "formatted")

# You can use keywords if you don't want to count.
print "{name} wants to eat {food}".format(name="Bob", food="lasagna")
