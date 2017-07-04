# Multiple inheritance

Multiple inheritance is when you define a class that inherits from one or more classes, like this:

    class SuperFun(Child, BadStuff):
        pass

Make a class named `SuperFun` that inherits from the classes `Child` and `BadStuff` at the same time.

n this case, whenever you have implicit actions on any `SuperFun` instance, Python has to look-up the possible function in the class hierarchy for both `Child` and `BadStuff`, but it needs to do this in a consistent order.

To do this Python uses "method resolution order" [(MRO)](http://python-history.blogspot.in/2010/06/method-resolution-order.html) and an algorithm called C3 to get it straight.

Because the MRO is complex and a well-defined algorithm is used, Python can't leave it to you to get the MRO right.
Instead, Python gives you the `super()` function, which handles all of this for you in the places that you need the altering type of actions as I did in `Child.altered`.
With `super()` you don't have to worry about getting this right, and Python will find the right function for you.

## `super` with `__init__`
The most common use of `super()` is actually in `__init__` functions in base classes. This is usually the only place where you need to do some things in a child, then complete the initialization in the parent. Here's a quick example of doing that in the `Child`:

    class Child(Parent):
        def __init__(self, stuff):
            self.stuff = stuff
            super(Child, self).__init__()

This is pretty much the same as the `Child.altered` example above, except I'm setting some variables in the `__init__` before having the `Parent` initialize with its `Parent.__init__`.
