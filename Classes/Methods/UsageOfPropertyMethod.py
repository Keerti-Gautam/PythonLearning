# We subclass from object to get a class.
class Human(object):
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. You should not invent such names on your own.
    
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property. If age isn't set then this value will be printed when called from instance
        self.age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    def grunt(self):
        return "*grunt*"
'''
    # Superficial thing here. Not really required.
    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

USAGE:
Use getter, setter and deleter for validation purposes, like if you want to do some calculation on numbers and return the result in a particular format than what was passed by the user as input.
'''

# Instantiate a class
i = Human(name="Ian")
print i.say("hi")  # prints out "Ian: hi"

j = Human("Joel")
print j.say("hello")  # prints out "Joel: hello"

# Call our class method
print i.get_species()  # => "H. sapiens"

# Change the shared attribute
Human.species = "H. neanderthalensis"
print i.get_species()  # => "H. neanderthalensis"
print j.get_species()  # => "H. neanderthalensis"

# Call the static method
print Human.grunt()  # => "*grunt*"

# Calling grunt using instant method
print i.grunt()

# Update the property
i.age = 42
print i.age
# Get the property
print i.age  # => 42

# Delete the property
del i.age
#i.age  # => raises an AttributeError
