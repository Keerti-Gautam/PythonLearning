# When to use what?

The question of "inheritance versus composition" comes down to an attempt to solve the problem of reusable code. You don't want to have duplicated code all over your software, since that's not clean and efficient.

Inheritance solves this problem by creating a mechanism for you to have implied features in base classes.
Composition solves this by giving you modules and the ability to call functions in other classes.

But what is more appropriate?

* Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.

* Use composition to package code into modules that are used in many different unrelated places and situations.

* Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.

**Do not be a slave to these rules.
Learn to adapt**
