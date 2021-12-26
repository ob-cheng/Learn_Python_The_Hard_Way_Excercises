from sys import argv
script, filename = argv

print(f"We are going to erase the {filename}.")
print("If you don't want to do it, press 'control C")
print("If you want to do it, hit RETURN.")

input("?")

print("Open the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("-----------------------\nnow I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()