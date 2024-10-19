try:
    raise NameError("Tis custom error message")
except NameError:
    print("caught exception")
    raise

