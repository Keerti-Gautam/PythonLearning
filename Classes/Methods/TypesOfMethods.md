# Methods

## Instance Methods

An instance method requires an instance in order to call it. This doesn't require any decorater.
`self` argument or parameter is a reference to that instance.
This is by far the most common type of method.
An instance method. All methods take "self" as the first argument

You call these using the name of the instance of a class (or object)
Let

    class Stuff(object):
      def add(self, x, y):
        return x+y

    S = Stuff()
    print S.add(2, 3)

Note that `S.add()` was used and not `Stuff.add()`

## Class Method

A class method is one that belongs to the class as a whole.
It doesn't require an instance. Instead, the class will automatically be sent as the first argument. A class method is shared among all instances.

A class method is declared with the `@classmethod` decorator.

    class Branch(object):
      branch = "Electronics and Comm."

      @classmethod
      def new_branch(cls):
        return cls.branch

    print Branch.new_branch()

Note that here class `Branch` `Branch.new_branch()` is used instead of an instance of the class.

## Static method

A static method is similar to a class method, but won't get the class object as an automatic parameter.
It is created by using the `@staticmethod` decorator.

    class Laugh(object):

      @staticmethod
      def hyena_laugh():
        return "*hehehehe*"

      #print Laugh.hyena_laugh("giggle")
      print Laugh.hyena_laugh()

Note that class name is used and the argument which is passed would not affect the output.

[Source](https://softwareengineering.stackexchange.com/a/306095)      
