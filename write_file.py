
# Write a line of code to create a file handle to open and append to a file called pelican.txt

pelicanfile = open("pelican.txt", 'a+')

# Append the following line to the file using the write method of the file handle:

line1 = "A wonderful bird is the pelican,\n"
pelicanfile.write(line1)

# Append the following second line using the write method:

line2 = "His bill holds more than his belican.\n"
pelicanfile.write(line2)

# Create a list that contains the following lines:

lines = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]

# Append this list to the file using the writelines method.

pelicanfile.writelines(lines)

pelicanfile.close()

# \n are required to produce new lines; after \n, the next string is displayed in a new line.
