# def cheese_and_cracker(cheese_count, boxes_of_cracker):
#     print(f"You have {cheese_count} cheeses and {boxes_of_cracker} boxes of cracker.")
#     print(f"Know that {boxes_of_cracker} boxes of cracker is a bit too much haha")
#
#
# print('------------------------')
#
# print("We can just give the function number directly.")
# cheese_and_cracker(20, 30)
#
# print('------------------------')
#
# print("Or we can use variables from script.")
# a = 20
# b = 30
# cheese_and_cracker(a, b)
#
# print('------------------------')
#
# print("We can do even math.")
# cheese_and_cracker(20 + 15, 40 - 10)
#
# print('------------------------')
#
# print("We can also combine the variables and math.")
# cheese_and_cracker(a + 100, b + 4)
# print("Enter the value of a")
# a = input('>')
# print("Enter the value of b")
# b = input('>')

def sq(a, b):
    print(f"the first variable is {a}")
    print(f"and the second variable is {b}")


sq(3, 2)

print("------------------------")

a = 'wow'
b = 'yes'
sq(a, b)

print("------------------------")


def fav(fav1, fav2):
    print(f"Your first favorite person is {fav1}.")
    print(f"And your second favorite person is {fav2}.")


fav1 = input('Enter your first favorite person.\n>')
fav2 = input('Enter your second favorite person.\n>')
fav(fav1, fav2)