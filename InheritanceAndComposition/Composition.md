# Composition

Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules, rather than rely on implicit inheritance. If you look at the three ways to exploit inheritance, two of the three _involve writing new code to replace or alter functionality_. This can easily be replicated by just calling functions in a module.

iting new code to replace or alter functionality. This can easily be replicated by just calling functions in a module. Here's an example of doing this:

    class Other(object):
        def override(self):
            print "OTHER override()"
        def implicit(self):
            print "OTHER implicit()"
        def altered(self):
            print "OTHER altered()"

    class Child(object):
        def __init__(self):
            self.other = Other()
        def implicit(self):
            self.other.implicit()
        def override(self):
            print "CHILD override()"
        def altered(self):
            print "CHILD, BEFORE OTHER altered()"
            self.other.altered()
            print "CHILD, AFTER OTHER altered()"

    son = Child()

    son.implicit() #OTHER implicit()
    son.override() #CHILD override()
    son.altered()
    # CHILD, BEFORE PARENT altered()
    # PARENT altered()
    # CHILD, AFTER PARENT altered()

In this code I'm not using the name `Parent`, since there is not a parent-child `is-a` relationship. This is a `has-a` relationship, where `Child` `has-a` `Other` that it uses to get its work done.

Most of the code in `Child` and `Other` is the same to accomplish the same thing. The only difference is that I had to define a `Child.implicit` function to do that one action.
