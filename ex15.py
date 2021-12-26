# import argv module
from fileinput import close
from sys import argv

script, filename = argv

# define txt
txt = open(filename)

print(f"Here is your file {filename}")
# open the file, and read the contents.
print(txt.read())

print("Type the filename again.")
file_again = input('>')

txt_again = open(file_again)

txt.close()
txt_again.close()