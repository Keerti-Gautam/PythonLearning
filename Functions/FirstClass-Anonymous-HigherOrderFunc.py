# Python has first class functions
def create_adder(x):
    def adder(y): #
        return x + y

    return adder # create_adder returns x+y

add_10 = create_adder(10) # 10+y is put in add_10
add_10(3)  # => 10+3 =13

# There are also anonymous functions
(lambda x: x > 2)(3)  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions


map(add_10, [1, 2, 3])  # => [11, 12, 13]
map(max, [1, 2, 3], [4, 2, 1])  # => [4, 2, 3]

filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]

# We can use list comprehensions for nice maps and filters
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x in 'abc'}  # Set => {'a', 'b', 'c'}
{x: x ** 2 for x in range(5)}  # Dict => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
