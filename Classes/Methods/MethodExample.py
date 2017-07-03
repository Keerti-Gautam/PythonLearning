#Instance Methods

class Stuff(object):
    def add(self, x, y):
        return x+y

S = Stuff()
print S.add(2, 3)

#classmethod

class Branch(object):
    branch = "Electronics and Comm."

    @classmethod
    def new_branch(cls):
        return cls.branch

print Branch.new_branch()

#staticmethod

class Laugh(object):
    @staticmethod
    def hyena_laugh():
        return "*hehehehe*"

print Laugh.hyena_laugh() #Should not give argument
