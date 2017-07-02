# Modules

Modules are like dictionaries.

    mystuff = {'apple': "I AM APPLES!"}
    print mystuff['apple']

So keep this idea of "getting X from Y" in your head and think about modules.
Modules are:

* A Python file with some functions or variables in it .
* You import that file.
* And you can access the functions or variables in that module with the . (dot) operator.

Let's say `mystuff.py` is a module with a function called apple in it.

    def apple():
        print "I AM APPLES!"

Once I have this code, I can use the module MyStuff with import and then access the apple function:

    import mystuff #Extension .py is not required
    mystuff.apple()

I could also put a variable in it named tangerine:

      def apple():
        print "I AM APPLES!"

      # this is just a variable
      tangerine = "Living reflection of a dream"

I can access that the same way:

    import mystuff
    mystuff.apple()
    print mystuff.tangerine

Refer back to the dictionary, and you should start to see how this is similar to using a dictionary, but the syntax is different. Let's compare:

    mystuff['apple'] # get apple from dict
    mystuff.apple() # get apple from the module
    mystuff.tangerine # same thing, it's just a variable

This means we have a very common pattern in Python:

* Take a key=value style container.
* Get something out of it by the key's name.

In the case of the dictionary, the key is a string and the syntax is `[key]`. In the case of the module, the key is an identifier, and the syntax is `.key`

Other than that they are nearly the same thing.

When you import a module there is only one for the entire program
