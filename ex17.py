from sys import argv
from os.path import exists
# type:" python3 ex17.py test.txt new_file.txt"
script, from_file, to_file = argv

print(f"copy from {from_file} to {to_file}.")

# We could do these two one line. How?
infile = open(from_file)
indata = infile.read()
# The len() function returns the number of items in an object.
print(f"The input file is {len(indata)} bytes long.")
print(f"Does the output file exist?\n >{exists(to_file)}")
print("Ready, hit RETURN; otherwise, hit CONTROL C to abort.")
input('?')

out_file = open(to_file, 'w')
out_file.write(indata)

print("All completed.")

out_file.close()
infile.close()
