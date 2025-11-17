class MyError(Exception):
    pass

try:
    raise MyError("My custom error occurred!")
except MyError as e:
    print(e)
