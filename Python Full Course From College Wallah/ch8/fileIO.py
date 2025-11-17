file = open("example.txt", "w")  # open file
file.write("Hello World")        # write data
file.close()                     # close file


file = open("example.txt", "r")
data = file.read()
print(data)
file.close()


file = open("example.txt", "a")
file.write("\nNew line added")
file.close()


with open("example.txt", "r") as file:
    data = file.read()
