#Exercises
"""
    We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function.
    Construct a small Python example to test whether this is possible, and write up your findings.
    Is a pair a generalization of a tuple, or is a tuple a generalization of a pair?
    Is a pair a kind of tuple, or is a tuple a kind of pair? """

def tuples_as_arguments(tuple_):
    for i in tuple_:
        print(i)


tup = (0, 1, 2, 3, 5, 6, 7, 8, 9)
tuples_as_arguments(tup)

