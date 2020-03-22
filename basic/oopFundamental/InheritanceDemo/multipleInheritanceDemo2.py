"""
.__init__ define super class so we need to assign "super(ClassName,parameter).__init__() "
"""

class First(object):
    def __init__(self):
        super(First, self).__init__()    #First class haven't any super class so if we don't declar ".__init__" , we haven't any problem
        print("first")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(Second, First):    # here we define multiple class in parameter, so it's happend multiple inheritance
    def __init__(self):
        super(Third, self).__init__()
        print("third")


Third()