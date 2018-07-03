def inner():
    return 1/0

def outer():
    return inner()

def more_outer():
    return outer()

more_outer()

