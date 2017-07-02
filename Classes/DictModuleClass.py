# Three ways to call things

# dict style
mystuff = {"apples": "Here are apples!"}
print mystuff['apples']

# module style
'''
In some module mystuff:

def apple():
print "I AM APPLES!"

# this is just a variable
tangerine = "Living reflection of a dream"
'''
#import the file
#mystuff.apples()
#print mystuff.tangerine

# class style
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine
