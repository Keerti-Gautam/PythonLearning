#For loops iterate over lists

for animal in ["dog", "cat", "mouse"]:
    # You can use {0} to interpolate formatted strings. (See above.)
    print "{0} is a mammal".format(animal) # It is perfect here as animal here is the first string and then cat and then mouse.

# Another way of writing the same loop
animal = ["dog", "cat", "mouse"] # Animal here is a list which requires different method of calling
for w in animal:
    print (w, len(w))
    x = animal.index(w)
    print "{} is a mammal".format(animal[x]) # Note that we cannot use animal as it will return all the animal names.
    print "{} is a mammal".format(w) # This will work fine because w which is the required string is returned.
    print "%s is a mammal"% animal[x] # Note that we cannot use w here as index because that is a string

for p in range(len(animal)):
    print "{} is definitely a mammal!".format(animal[p])

words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire lis
    if len(w) > 6:
      words.insert(0, w) # Tries to insert defenestrate over and over again in the array
      print words

for x in range(11,0, -1):
    print x
