a = 1
print("Hello World")

1_error = "Bye"

def start():
    bar()


def bar():
    return test()


def test():
    return bar()


def baz():
    return bar()


start()
