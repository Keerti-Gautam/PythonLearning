# Classes

You can think about a module as a specialized dictionary that can store Python code so you can access it with the . operator.

Python also has another construct that serves a similar purpose called a class. A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

If I were to create a class just like the mystuff module, I'd do something like this:

    class MyStuff(object):
      def __init__(self):
        self.tangerine = "And now a thousand years between"
      def apple(self):
        print "I AM CLASSY APPLES!"

That looks complicated compared to modules, but you should be able to make out how this is like a "mini-module" with `MyStuff` having an apple() function in it. What is probably confusing is the `__init__()` function and use of `self.tangerine` for setting the tangerine instance variable.

Here's why classes are used instead of modules:
You can take this MyStuff class and use it to craft many of them, millions at a time if you want, and each one won't interfere with each other. When you import a module there is only one for the entire program unless you do some monster hacks.

Before you can understand this though, you need to know what an "object" is and how to work with MyStuff just like you do with the `mystuff.py` module.

## Objects are Like Import

If a class is like a "mini-module," then there has to be a similar concept to import but for classes. That concept is called "instantiate", which is just a fancy, obnoxious, overly smart way to say "create." When you instantiate a class what you get is called an object.

You instantiate (create) a class by calling the class like it's a function, like this:

    thing = MyStuff()
    thing.apple()
    print thing.tangerine

The first line is the "instantiate" operation, and it's a lot like calling a function. However, Python coordinates a sequence of events for you behind the scenes. I'll go through these steps using the above code for MyStuff:

1. Python looks for `MyStuff()` and sees that it is a class you've defined.
2. Python crafts an empty object with all the functions you've specified in the class using `def`.
3. Python then looks to see if you made a "magic" `__init__` function, and if you have, it calls that function to initialize your newly created empty object.
4. In the `MyStuff` function `__init__`, I then get this extra variable self, which is that empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
5. In this case, I set `self.tangerine` to a song lyric and then I've initialized this object.
6. Now Python can take this newly minted object and assign it to the thing variable for me to work with.

#### Why use `self` while making `__init__` or other functions?

Without `self` the code isn't clear about whether you mean the instance's `tangerine` attribute, or a local variable named `tangerine`. With `self.tangerine = 'Some lyrics'` it's very clear you mean the instance attribute `self.tangerine`.

That's the basics of how Python does this "mini-import" when you call a class like a function. Remember that this is not giving you the class, but instead is using the class as a blueprint for building a copy of that type of thing.

Keep in mind that I'm giving you a slightly inaccurate idea for how these work so that you can start to build up an understanding of classes based on what you know about modules.

The truth is, classes and objects suddenly diverge from modules at this point.
If I were being totally honest, I'd say something more like this:

* Classes are like blueprints or definitions for creating new mini-modules.
* Instantiation is how you make one of these mini-modules and import it at the same time. "Instantiate" just means to create an object from the class.
* The resulting created mini-module is called an object and you then assign it to a variable to work with it.

At this point objects behave differently from modules and this should only serve as a way for you to bridge over to understanding classes and objects.
