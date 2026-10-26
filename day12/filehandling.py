# File Handling:

# open a file
# open("file path", 'mode to open file')

# read mode('r'): used to read the data from the file, file should exists in the defined path
# f = open('day12/file.txt', "r") # use / or \\
# a = f.read()
# print(a)
# f.close()

# write mode('w'): used to write in a file, if the define file does not exist a file is created, if file exists previous data is replaced by new data
f = open('day12/file.txt', "w")
f.write()
# a = f.write(" Writing mode ") # counts space as well
# print(a)
# f.close()

# append mode(a): used to write in a file, if the define file does not exist a file is created, if file exists new data is added at the end of previous data
# f = open('day12/file.txt', "a")
# a = f.write(" Editig a file ")
# print(a)
# f.close()
