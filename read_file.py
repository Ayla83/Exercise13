
# Use the open and read methods to slurp the entire contents of your pelican.txt file

pelicanfile = open("pelican.txt", 'r')
contents = pelicanfile.read()
print("The contents of the file are: ")
print(contents)

# Display the type of the returned data and print the contents of the returned data

print("The data type is: ", type(contents))

# What data type is the output?
# It's a string.

print("**********************")

# Write some code that will read the pelican.txt file into a list
# and then output the number of items within the list

pelicanfile2 = open("pelican.txt", 'r')
pelicanlist = pelicanfile2.readlines()
print("The lines of the files as a list are: ")
print(pelicanlist)
print("The number of items in this list is: ", len(pelicanlist))

# Use a loop to iterate over and print the contents of the file.
# Be sure not to include any blank lines in the output.
print("**********************")
print("Printing the contents of the file iteratively:")
for line in open("pelican.txt"):
    print(line, end="")

# The "end" parameter prevents an additional new line from being printed
