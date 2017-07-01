# Dictionaries store mappings
print "Format of dictionaries are dict_name = {key1: value1, key2: value2, ....} where keys should be written in double quotes."

empty_dict = {}

# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values of particular keyps with ["particular-key"]
print filled_dict["one"]  # => 1

# Get all keys as a list with "keys()"
print filled_dict.keys()  # => ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed. The results might not match this.

# Get all values as a list with "values()"
print filled_dict.values()  # => [3, 2, 1]
# Note - Same as above regarding key ordering.

# Get all key-value pairs as a list of tuples with "items()"
print filled_dict.items()  # => [("one", 1), ("two", 2), ("three", 3)]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict  # => False

# Looking up a non-existing key is a KeyError
#filled_dict["four"]  # KeyError ans key = four doesn't exist

# Use "get()" method to avoid the KeyError. The get method supports a default argument when the value is missing.
# Format is dict_name.get(key, default=None) where key is the key to be searched and default is the value which should be returned in case key isn't found.
print filled_dict.get("one")  # => 1
print filled_dict.get("four")  # => None

# Using default values
print filled_dict.get("one", 4)  # => 1
print filled_dict.get("four", 4)  # => 4
# note that filled_dict.get("four") is still => None
# (get doesn't set the value in the dictionary)

# set the value of a key with a syntax similar to lists
filled_dict["four"] = 4  # now, filled_dict["four"] => 4
print filled_dict

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
print filled_dict
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5
print filled_dict
