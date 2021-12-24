# from sys import argv
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is", third)
from sys import argv

# read the WYSS section for how to run this
script, a, b, c = argv
a = input()
b = input()
c = input()
print("The script is called:", script)
print("Your first variable is:", a)
print("Your second variable is:", b)
print("Your third variable is:", c)

# It's not asking you to run in Pycharm. You need to use terminal to run this code, and then it wont show you error
# message.
