from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("This script is to practice what I learned in ex17.")
print("\nLet's open the original file. Ready? press Enter.")
input('ENTER')

file1 = open(from_file)
indata = file1.read()

print(f"Now we are going to input the data to {to_file}")
file2 = open(to_file, 'w')
file2.write(indata)

print(f"Okay, let's see if the new file exists.\n{exists(to_file)}")
if exists(to_file):
    print("Alright! Complete!")
else:
    print("Something wrong with your code. Recheck.")