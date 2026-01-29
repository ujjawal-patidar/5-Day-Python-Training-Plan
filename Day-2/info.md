
# we can pass generator as an argument to these constructors, also the parameter which are accepting iterables as a parameter can accept the generator also (although generator is a iterator but its iterable also)

List: list(x for x in range(5)) creates [0, 1, 2, 3, 4].
Tuple: tuple(x for x in range(5)) creates (0, 1, 2, 3, 4).
Dict: dict((i, i**2) for i in range(3)) creates {0: 0, 1: 1, 2: 4}

