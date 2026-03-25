# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open("myFile.txt", "w")

# Get some info
print("Name of the file: ", myFile.name)
print("Is closed: ", myFile.closed)
print("Opening mode: ", myFile.mode)

# Write to the file
myFile.write("I love Python")
myFile.write(" and Bash scripting")
myFile.close()

# Append to file
myFile = open("myFile.txt", "a")
myFile.write(" and I also love Golang")
myFile.close()

# Read from file
myFile = open("myFile.txt", "r+")
text = myFile.read(100)
print(text)
myFile.close()
