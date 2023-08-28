def cons(a, b):
    def pair(f):
        return f(a, b) 
    return pair

# This is a different type of question than Im used to
# My instict is to run through examples but that doesn't make sense in this scenario
# The way they've defined it is I'm assumigng based off of some functional paradigm?
# It's hard to fully grasp this probelm without understanding what exactly is the purpose of f (that being a function being passed to another function).
# also since pair is passed an argument(f) when defined how can we return it without passing any arguments, this gives me extending a class based energy, but obviously
# we're not doing any sort of extending classes here.

