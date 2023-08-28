# this one is like your scripts with argv

# Here *args takes 3 arguments as an input
def print_three(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

# Here *args takes 2 arguments as an input
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():
    print("I got nothin'.")




print_two("Harry","Porter")
print_two_again("Harry2","Porter2")
print_three("Harry","Ron","Emma")
print_one("First!")
print_none() 

"""
Using *args we can pass any number of arguments to the python function.
Later the list should be unpacked.

"""