# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")


# okay, that *arg is actually pointless. We can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}.")


# this just take one argument.
def print_one(arg1):
    print(f"arg1:{arg1}.")


# this takes no argument.
def print_none():
    print("this got nothing.")


print_two("Free", "Belarus")
print_two_again("Free", "Bela-russia")
print_one("Freedoms")
print_none()
