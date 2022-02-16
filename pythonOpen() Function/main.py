read_file = open("Python.txt", "w")
read_file.write("I Love Python")
read_file.close()
read_file = open("Python.txt","r")
print(read_file.read())

