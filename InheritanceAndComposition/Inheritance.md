# Inheritance

Inheritance is used to indicate that one class will get most or all of its features from a parent class.
This happens implicitly whenever you write class `Foo(Bar)`, which says "Make a class Foo that inherits from Bar."
When you do this, the language makes any action that you do on instances of `Foo` also work as if they were done to an instance of `Bar`.
Doing this lets you put common functionality in the `Bar` class, then specialize that functionality in the `Foo` class as needed.

_**Most of the uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs.**_

There are three ways Parents and Child can interact:

* Actions on the child imply an action on the parent.
* Actions on the child alter the action on the parent.
* Actions on the child override the action on the parent.

## Implicit Inheritance
Implicit actions happen when you define a function in the parent, but not in the child.

**Note: Override, implicit and altered are not built in functions in python but are so named so that you know which one was being talked about. It is totally your choice to name them with whatever you want. Any name of the function works.**

    class Parent(object):
        def implicit(self):
          print "PARENT implicit()"

    class Child(Parent):
        pass

    dad = Parent()
    son = Child()

    dad.implicit() # PARENT implicit()
    son.implicit() # PARENT implicit()

`pass` statement does nothing particular but can act as a placeholder, or here, let's python know that you want an empty block. That is, there's nothing new to define in it. Instead it will inherit all of its behavior from `Parent`

## Override Explicitly

Sometimes you want the `child` to behave differently. In this case you want to override the function in the child, effectively replacing the functionality.
To do this you define a function with the same name in `Child`.

    class Parent(object):
        def override(self):
            print "PARENT override()"

    class Child(Parent):
        def override(self):
            print "CHILD override()"

    dad = Parent()
    son = Child()

    dad.override() # PARENT override()
    son.override() # CHILD override()

Here, `Child` overrides the statement function of `parent` by defining its own version or functionality of it.

## Altering Parent Actions

A special case of overriding is where you want to alter the behavior of `Parent` before or after the `Parent` class's version runs.
You first override the function just like in the last example, but then you use a Python built-in function named `super` to get the Parent version to call.

    class Parent(object):
        def altered(self):
            print "PARENT altered()"

    class Child(Parent):
        def altered(self):
            print "CHILD, BEFORE PARENT altered()"
            super(Child, self).altered()
            print "CHILD, AFTER PARENT altered()"

    dad = Parent()
    son = Child()

    dad.altered() # PARENT altered()
    son.altered() # prints "CHILD, BEFORE PARENT altered()", then "PARENT altered()" and finally "CHILD, AFTER PARENT altered()"

After the first statement on statement function of class Child is run, we want the parent's version to run. For that we use Python built in function super.
Super is aware of the inheritance of Child from father and will get the Parent class for you.

It may be read as "call `super` with arguments `Child` and `self`, then call the function `statement` on whatever it returns." And at this point, `Parent` statement function runs and prints out `Parent` message.
